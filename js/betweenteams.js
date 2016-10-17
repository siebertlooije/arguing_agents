window.onload = function()
{
    make_selects();

    $("#logbetween").val("");

    $("button#buttonstart").on('click', function ()
    {

        $("#logbetween").val("");
        competition = make_teams();
        index_round_club = 0;
        make_graph(competition);
        log_clubs(competition);
    });

    $("button#buttonnext").on('click',function ()
    {
        if(index_round_club == competition.length - 1)
            index_round_club = 0;

        round(competition, index_round_club);
        index_round_club ++;
    })

    $("#buttontable").on("click", function()
    {
        for(var index = 0; index != competition.length; index++)
        {

            var club = competition[index]
            $('#show_table > tbody:last-child').append('<tr class="child"><td>hallo</td></tr>');
            //for(var index2 = 0; index2 != club.players.length; index2++)
            //{
             //   table.after('<td>')
              /*  table.after(club.players[index2].name)
                table.after('</td>')
                table.after('<td>')
                table.after(club.players[index2].att)
                table.after('</td>')
                table.after('<td>')
                table.after(club.players[index2].def)
                table.after('</td>')
                table.after('<td>')
                table.after(club.players[index2].price)
                table.after('</td>')
            }*/
        }
        location.href = "teamselection.htm"

    })


};

function make_selects()
{
    for(var i=2; i<6; i++)
    {
        $("select#numberofteams").append($('<option>',
         {
                value:i,
                text: i.toString()
         }))
    }
}

function read_in_names()
{
    var names = []
    $.ajax({
        type: "GET",
        url: "../js/footballers.csv",
        dataType: "text",
        success: function(data)
        {
           names = processNames(data);
        },
        async: false
     });
    return names;
}

function processNames(Text)
{
    var allTextLines = Text.split(/\r\n|\n/);
    var lines = [];
    for (var index = 1; index != allTextLines.length ; index ++)
    {
        var items = allTextLines[index].split(',')
        var name = items[1]
        lines[index - 1] = name;
    }
    return lines;
}

function create_players(name)
{
    var att = Math.random() *15;
    var def = Math.random() *15;
    var player = {
       att: att,
       def: def,
       price: (att + def)*Math.random(),
       name: name,
       attrib: att + def
   }
   return player;
}

function create_transferlist(num_clubs, names)
{
    var players = []
    var counter = 0
    for(var index = num_clubs* 15 ; index !=names.length ; index++)
    {

        players[counter] = create_players(names[index])
        counter++
    }
    var transfer_list =
    {
        name: "transfer list",
        players:players
    }
    return transfer_list
}

function create_team(team_name, index_team, player_names)
{
    var players = []
    for(var index = 0; index != 15; index ++)
    {
         players[index] = create_players(player_names[(index_team*15) + index]);
    }

    var team =
    {
        name: team_name,
        number_of_players: 15,
        players: players,
        budget:  Math.random()* 100,
        bids:[]
    };
    return team
}

function make_teams()
{
    var competition = []
    var team_array = ["ajax", "feyenoord","psv", "zwolle", "heerenveen"]
    var numb_teams = $("select#numberofteams").val();
    var player_names = read_in_names();
    for (var index = 0; index != numb_teams; index++)
    {
        competition[index] = create_team(team_array[index], index, player_names)
    }
    competition[competition.length] = create_transferlist(competition.length, player_names);
    return competition;
}