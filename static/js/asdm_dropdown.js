$(document).ready(function(){
  // Films specific //
        $("#btn-film-all").click(function(){
             var OPT = new Array("all");
                $("#film-choice-dropdown").find('option').remove();
                for(i=0; i < OPT.length; i++){
                     $("#film-choice-dropdown").append('<option value="'+OPT[i]+'">'+OPT[i]+'</option>');
                 }
        });
        $("#btn-film-title").click(function(){
             var OPT = new Array("Dolittle","JoJo Rabbit","Little Women","Amarcord");
                $("#film-choice-dropdown").find('option').remove();
                for(i=0; i < OPT.length; i++){
                     $("#film-choice-dropdown").append('<option value="t'+OPT[i]+'">'+OPT[i]+'</option>');
                 }
        });
        $("#btn-film-genre").click(function(){
             var OPT = new Array("Family","Action","Comedy","Drama");
                $("#film-choice-dropdown").find('option').remove();
                for(i=0; i < OPT.length; i++){
                     $("#film-choice-dropdown").append('<option value="g'+OPT[i]+'">'+OPT[i]+'</option>');
                 }
        });
        $("#btn-film-age").click(function(){
             var OPT = new Array("U","PG","12A","15");
                $("#film-choice-dropdown").find('option').remove();
                for(i=0; i < OPT.length; i++){
                     $("#film-choice-dropdown").append('<option value="a'+OPT[i]+'">'+OPT[i]+'</option>');
                 }
        });
        // Restaurants //
        $("#btn-rest-all").click(function(){
             var OPT = new Array("N/A");
                $("#rest-choice-dropdown").find('option').remove();
                for(i=0; i < OPT.length; i++){
                     $("#rest-choice-dropdown").append('<option value="'+OPT[i]+'">'+OPT[i]+'</option>');
                 }
        });
        $("#btn-rest-name").click(function(){
             var OPT = new Array("all",
                "Bella Italia",
                "Buffalo Grill",
                "Burger Bite",
                "Cafe Kerno",
                "Chaopraya",
                "Cosmo",
                "Costa Coffee",
                "Edinburgh Larder",
                "Hard Rock Cafe",
                "Kweilin",
                "La Piazza",
                "Michael's Steak & Seafood Bar",
                "Passage of India",
                "Pizza Express",
                "Pizza Hut",
                "Starbucks",
                "TGI Friday's",
                "Thai Orchid",
                "The Mussel and Steak bar",
                "Ting Thai Caravan",
                "Wagamama",
                "Xiangbala Hotpot"
             );
                $("#res-choice-dropdown").find('option').remove();
                for(i=0; i < OPT.length; i++){
                     $("#rest-choice-dropdown").append('<option value="n'+OPT[i]+'">'+OPT[i]+'</option>');
                 }
        });
        $("#btn-rest-type").click(function(){
             var OPT = new Array("all",
              "American Classics",
             "Coffee shop",
             "Italian cuisine",
             "Pan-Asian cuisine");
                $("#rest-choice-dropdown").find('option').remove();
                for(i=0; i < OPT.length; i++){
                     $("#rest-choice-dropdown").append('<option value="t'+OPT[i]+'">'+OPT[i]+'</option>');
                 }
        });
        // Buses
        $("#btn-route-one").click(function(){
             var OPT = new Array("any",
              "Bruntsfield Place",
              "Elm Row",
              "Fountainbridge",
              "King's Theatre",
              "Lothian Rd",
              "Princes Street West",
              "Scotts Monument",
              "Shrubhill",
              "St. Andrew",
              "Usher Hall",
              "Whitehouse Loan",
              "York Place");
              $("#bus-choice-dropdown").find('option').remove();
              for(i=0; i < OPT.length; i++){
                   $("#bus-choice-dropdown").append('<option value="'+OPT[i]+'">'+OPT[i]+'</option>');
              }
      });
      $("#btn-route-two").click(function(){
           var OPT = new Array("any",
           "Blacket Ave",
           "Clerk St",
           "Dean St",
           "E Preston St",
           "Hamilton Place",
           "Hill Place",
           "Howe St",
           "North Bridge",
           "Princes Street (West)",
           "Rose St",
           "Royal Circus",
           "South Bridge",
           "Thistle Street",
           "Ventnor Ter",
           "Wilton Rd");
            $("#bus-choice-dropdown").find('option').remove();
            for(i=0; i < OPT.length; i++){
                 $("#bus-choice-dropdown").append('<option value="'+OPT[i]+'">'+OPT[i]+'</option>');
            }
    });
    // Shops
    $("#btn-shop-all").click(function(){
         var OPT = new Array("N/A");
            $("#shop-choice-dropdown").find('option').remove();
            for(i=0; i < OPT.length; i++){
                 $("#shop-choice-dropdown").append('<option value="'+OPT[i]+'">'+OPT[i]+'</option>');
             }
    });
    $("#btn-shop-name").click(function(){
         var OPT = new Array("any",
        "Apple Store",
        "Apple pharmacy",
        "Blackwells",
        "Boots",
        "Harvey Nichols",
        "Heritage of Edinburgh",
        "Hollister",
        "JD Sports",
        "Jeffrey Street",
        "John Lewis",
        "Kitchens Defined",
        "Mediterranean Supermarket",
        "Mobile Care Point",
        "Prestige Scotland",
        "Primark",
        "Real Scot Shop",
        "Sainsbury's Local",
        "Sports Direct",
        "Tesco Express",
        "Timberland",
        "Waterstones",
        "Waverly Mall",
        "Whisky World",
        "Zara");
          $("#shop-choice-dropdown").find('option').remove();
          for(i=0; i < OPT.length; i++){
               $("#shop-choice-dropdown").append('<option value="n'+OPT[i]+'">'+OPT[i]+'</option>');
          }
      });
      $("#btn-shop-type").click(function(){
           var OPT = new Array("any",
           "Alcoholic beverages",
           "Book store",
           "Department Store",
           "Drugstore/Pharmacy",
           "Electronics retail",
           "Fashion/clothing store",
           "Retail/outdoor wear",
           "Shopping Mall",
           "Supermarket",
           "Tourist shop"
         );
        $("#shop-choice-dropdown").find('option').remove();
        for(i=0; i < OPT.length; i++){
             $("#shop-choice-dropdown").append('<option value="c'+OPT[i]+'">'+OPT[i]+'</option>');
        }
      });
      // Parking
      $("#btn-park-dist").click(function(){
           var OPT = new Array("50","100","150","200","250","300","350","400","450","500"
         );
        $("#park-dist-choice-dropdown").find('option').remove();
        for(i=0; i < OPT.length; i++){
             $("#park-dist-choice-dropdown").append('<option value="'+OPT[i]+'">'+OPT[i]+'</option>');
        }
      });
      // Districts
      $("#btn-dist-in").click(function(){
           var OPT = new Array(
             "Abbeyhill",
             "Bellevue/Broughton",
             "Bonnington",
             "Broughton Rd/Powderhall",
             "Bruntsfield",
             "Calton Hill",
             "Canongate",
             "Canonmills",
             "Churchill and Greenhill",
             "Comely Bank",
             "Craigentinny",
             "Craigleith",
             "Crewe Toll",
             "Dalry",
             "Dean Village/West End",
             "Duddingston Village and Golf Course",
             "Dumbiedykes",
             "Ferryfield/Inverleith",
             "Fettes",
             "Fountainbridge",
             "Fountainbridge/Polwarth",
             "Gayfield/Broughton St",
             "Goldenacre",
             "Gorgie",
             "Grange",
             "Haymarket",
             "Hillside/Easter Rd",
             "Holyrood Park",
             "Hutchison/Slateford",
             "Inverleith",
             "Lauriston/Quartermile",
             "Leith",
             "Leith Links",
             "Leith/Easter Rd",
             "Lochend",
             "Marchmont",
             "Marionville",
             "Meadowbank",
             "Merchiston and Myreside",
             "New Town",
             "Newington",
             "Northfield",
             "Old Town",
             "Orchard Brae",
             "Peffermill",
             "Piershill/Piersfield",
             "Pilrig",
             "Polwarth",
             "Prestonfield",
             "Ravelston/Murrayfield",
             "Restalrig",
             "Roseburn",
             "Sciennes",
             "Seafield",
             "Shandon",
             "Southside",
             "St Leonards",
             "Stockbridge",
             "Tollcross",
             "Viewforth",
             "Warriston",
             "West End",
             "Wester Coates",
             "Willowbrae"
         );
        $("#district-choice-dropdown").find('option').remove();
        for(i=0; i < OPT.length; i++){
             $("#district-choice-dropdown").append('<option value="'+OPT[i]+'">'+OPT[i]+'</option>');
        }
      });
      $("#btn-dist-adj").click(function(){
           var OPT = new Array(
             "Abbeyhill",
             "Bellevue/Broughton",
             "Bonnington",
             "Broughton Rd/Powderhall",
             "Bruntsfield",
             "Calton Hill",
             "Canongate",
             "Canonmills",
             "Churchill and Greenhill",
             "Comely Bank",
             "Craigentinny",
             "Craigleith",
             "Crewe Toll",
             "Dalry",
             "Dean Village/West End",
             "Duddingston Village and Golf Course",
             "Dumbiedykes",
             "Ferryfield/Inverleith",
             "Fettes",
             "Fountainbridge",
             "Fountainbridge/Polwarth",
             "Gayfield/Broughton St",
             "Goldenacre",
             "Gorgie",
             "Grange",
             "Haymarket",
             "Hillside/Easter Rd",
             "Holyrood Park",
             "Hutchison/Slateford",
             "Inverleith",
             "Lauriston/Quartermile",
             "Leith",
             "Leith Links",
             "Leith/Easter Rd",
             "Lochend",
             "Marchmont",
             "Marionville",
             "Meadowbank",
             "Merchiston and Myreside",
             "New Town",
             "Newington",
             "Northfield",
             "Old Town",
             "Orchard Brae",
             "Peffermill",
             "Piershill/Piersfield",
             "Pilrig",
             "Polwarth",
             "Prestonfield",
             "Ravelston/Murrayfield",
             "Restalrig",
             "Roseburn",
             "Sciennes",
             "Seafield",
             "Shandon",
             "Southside",
             "St Leonards",
             "Stockbridge",
             "Tollcross",
             "Viewforth",
             "Warriston",
             "West End",
             "Wester Coates",
             "Willowbrae"
         );
        $("#district-choice-dropdown").find('option').remove();
        for(i=0; i < OPT.length; i++){
             $("#district-choice-dropdown").append('<option value="'+OPT[i]+'">'+OPT[i]+'</option>');
        }
      });
      $("#btn-dist-not-in").click(function(){
           var OPT = new Array(
             "Abbeyhill",
             "Bellevue/Broughton",
             "Bonnington",
             "Broughton Rd/Powderhall",
             "Bruntsfield",
             "Calton Hill",
             "Canongate",
             "Canonmills",
             "Churchill and Greenhill",
             "Comely Bank",
             "Craigentinny",
             "Craigleith",
             "Crewe Toll",
             "Dalry",
             "Dean Village/West End",
             "Duddingston Village and Golf Course",
             "Dumbiedykes",
             "Ferryfield/Inverleith",
             "Fettes",
             "Fountainbridge",
             "Fountainbridge/Polwarth",
             "Gayfield/Broughton St",
             "Goldenacre",
             "Gorgie",
             "Grange",
             "Haymarket",
             "Hillside/Easter Rd",
             "Holyrood Park",
             "Hutchison/Slateford",
             "Inverleith",
             "Lauriston/Quartermile",
             "Leith",
             "Leith Links",
             "Leith/Easter Rd",
             "Lochend",
             "Marchmont",
             "Marionville",
             "Meadowbank",
             "Merchiston and Myreside",
             "New Town",
             "Newington",
             "Northfield",
             "Old Town",
             "Orchard Brae",
             "Peffermill",
             "Piershill/Piersfield",
             "Pilrig",
             "Polwarth",
             "Prestonfield",
             "Ravelston/Murrayfield",
             "Restalrig",
             "Roseburn",
             "Sciennes",
             "Seafield",
             "Shandon",
             "Southside",
             "St Leonards",
             "Stockbridge",
             "Tollcross",
             "Viewforth",
             "Warriston",
             "West End",
             "Wester Coates",
             "Willowbrae"
         );
        $("#district-choice-dropdown").find('option').remove();
        for(i=0; i < OPT.length; i++){
             $("#district-choice-dropdown").append('<option value="'+OPT[i]+'">'+OPT[i]+'</option>');
        }
      });
});
