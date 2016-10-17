/**
 * Created by siebert on 17-10-16.
 */

function log_refuse_bid(club1_name, club2_name, playername , bid )
{
    var log = "Club : " +club2_name + "refused bid :" + bid +" on " + playername + " of club :" + club1_name + " because too low bid"
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

function log_bid(player,club1_name, club2_name, bid)
{
    var log = "Club : " + club1_name + " make bid :" + bid + " on player "+ player.name + " from club : " + club2_name;
    write_log(log)
}


function write_log(log_text)
{
    var prev_log = $("#logbetween").val()
    $("#logbetween").val(prev_log + log_text + "\n");
}
