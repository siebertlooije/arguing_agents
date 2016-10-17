/**
 * Created by siebert on 17-10-16.
 */

function log_refuse_bid(club1_name, club2_name, playername , bid )
{
    var log = "Club : " +club2_name + " refused bid :" + bid +" on " + playername + " of club :" + club1_name + " because too low bid"
    write_log(log)
}

function log_clubs(competition)
{
    var log = "The competition starts with :"
    var teams_log = competition[0].name;
    for(var index = 1; index != competition.length; index ++)
    {
        teams_log = teams_log + "," +  competition[index].name
    }
    write_log(log + teams_log)
}

function log_sold(playername, club1_name, club2_name, bid)
{
    var log = "Club : " + club2_name + " sold "+ bid + " player "+ playername + " to club : " + club1_name;
    write_log(log)
}

function log_bid(player,club1_name, club2_name, bid, inter_president, strategie)
{

    var log = "Club used : " + strategie_reason(strategie)
    write_log(log)

    log = "Club : " + club1_name + " make bid :" + bid + " on player "+ player.name + " from club : " + club2_name;
    write_log(log)

    if(inter_president)
    {
        log = "President of club : " + club2_name + " stopped the bid because : " + random_reason()
        write_log(log)
    }

}

function strategie_reason(strategie)
{
    switch(true)
    {
        case (strategie < 0.33):
            return "strategie : best player of the club"
        case (strategie >= 0.33 && strategie < 0.66):
            return "strategie : random player of random club"
        case (strategie >= 0.66):
            return "strategie : baddest player of the club";
    }
}

function random_reason()
{
    var random_num = Math.random()
    switch(true)
    {
        case (random_num < 0.25):
            return "the player is too good"
        case (random_num >= 0.25 && random_num < 0.5):
            return "the player is a good friend"
        case (random_num >= 0.5 && random_num < 0.75):
            return "the player married my daughter"
        case (random_num >= 0.75):
            return "scored a lot of goals previous year"
        default:
            return "no specific reason"
    }
}


function write_log(log_text)
{
    var prev_log = $("#logbetween").val()
    $("#logbetween").val(prev_log + log_text + "\n");
}
