/**
 * Created by siebert on 17-10-16.
 */




function round(competition, index_club)
{
    var club = competition[index_club];
    write_log("ROUND : " + club.name);
    check_bids(club, index_club, competition);

    var array_strategie = club_strategie(competition,club);
    var strategie = array_strategie[1]
    var array_player = array_strategie[0]
    var player = array_player[0];
    if(player == null)
    {
        write_log("This round nothing happens")
        return;
    }
    var club_index = array_player[1];
    var bid = (player.price *(Math.random() * 2 ));

    var inter_president = check_interruption_president()

    log_bid(player,club.name, competition[club_index].name, bid, inter_president, strategie);
    make_bid(player,index_club, club_index, bid, inter_president);
    set_bid(player,club,club_index, bid);
}

function club_strategie(competition, club)
{
    var random_num = Math.random()
    switch(true)
    {
        case (random_num < 0.33):
            return [find_player(competition,club, true),random_num]
        case (random_num >= 0.33 && random_num < 0.66):
            return [random_player(competition,club), random_num]
        case (random_num >= 0.66):
            return [find_player(competition,club,false),random_num];
    }
}


function check_interruption_president()
{
    if(Math.random() < 0.05)
        return true;
    return false;
}

function check_bids(club1, index_club, competition)
{
    if(club1.bids.length == 0)
        return;
    for(var index = 0; index != club1.bids.length; index ++)
    {
        if(club1.bids[index]["Bid"] >= club1.bids[index]["Pvalue"])
        {
            var club2index = club1.bids[index]["Club"]
            log_sold(club1.bids[index]["Player"],  club1.name,competition[club2index].name, club1.bids[index]["Bid"]);
            add_sold(club1.bids[index]["Player"], club2index, index_club, club1.bids[index]["Bid"])
            remove_bid(club1.bids[index]["Player"],club1.bids[index]["Club"])
            buy_player(club1.bids[index]["Player"],club1,competition[club2index])
            sell_player(club1.bids[index]["Player"], club1)
        }
        else
        {
            log_refuse_bid(club1.name, competition[club1.bids[index]["Club"]].name, club1.bids[index]["Player"], club1.bids[index]["Bid"])
            add_refuse(club1.bids[index]["Player"],club1.bids[index]["Club"],club1.bids[index]["Bid"])
            remove_bid(club1.bids[index]["Player"],club1.bids[index]["Club"])
        }
    }
}

function buy_player(playername, club1, club2)
{
    for(var index=0; index!= club1.players.length;index ++)
    {
        if(club1.players[index].name == playername)
            club2.players.push(club1.players[index])
    }
}

function sell_player(playername, club)
{
    for(var index = 0; index != club.players.length; index ++)
    {
        if(playername == club.players[index].name)
            club.players.splice(index,1)
    }
}

function set_bid(player, club1, club2index, bid)
{
    var bid = {"Player" : player.name, "Club" : club2index , "Bid": bid, "Pvalue": player.price}
    club1.bids.push(bid)
}

function find_best_player(players)
{
    var best_player_attri = 0;
    var best_player = null;
    for (var index1 = 0; index1 != players.length; index1++)
    {

        if (best_player_attri < players[index1].attrib)
        {
            best_player_attri = players[index1].attrib
            best_player = players[index1]
        }
    }
    return best_player
}

function find_baddest_player(players)
{
    var bad_player_attri = 999;
    var bad_player = null;
    for (var index1 = 0; index1 != players.length; index1++)
    {

        if (bad_player_attri > players[index1].attrib)
        {
            bad_player_attri = players[index1].attrib
            bad_player = players[index1]
        }
    }
    return bad_player
}


function random_player(competition,club)
{
    while(true)
    {
        var club_random =  getRandomInt(0, competition.length - 1)
        var player_random = getRandomInt(0,15)
        if(competition[club_random].name == club.name)
            continue;

        return [competition[club_random].players[player_random], club_random]
    }
}

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function find_player(competition, club, best)
{
    var player = null;
    var player_index = null
    for(var index = 0; index != competition.length; index++)
    {
        if(competition[index].name == club.name)
            continue
        if(best)
        {
            var temp_player = find_best_player(competition[index].players)

            if (player == null || temp_player.attrib > player.attrib)
            {
                player = temp_player;
                player_index = index;
            }
        }
        else
        {
            var temp_player = find_baddest_player(competition[index].players)

            if (player == null || temp_player.attrib < player.attrib)
            {
                player = temp_player;
                player_index = index;
            }
        }
    }
    return [player,player_index]
}
