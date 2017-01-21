

   var data = [
                    {
                     "name": "Rehan",
                     "location": "Pune",
                     "description": "hello hi",
                     "created_by": 13692,
                     "users_name": "xyz",
                    },
                    {
                      "name": "Sameer",
                      "location": "Bangalore",
                      "description": "how are you",
                      "created_by": 13543,
                      "users_name": "abc",
                    },
                ]

            var htmlText = '';

            for ( var key in data ) {
                htmlText += '<div class="div-conatiner">';
                htmlText += '<p class="p-name"> Name: ' + data[key].name + '</p>';
                htmlText += '<p class="p-loc"> Location: ' + data[key].location + '</p>';
                htmlText += '<p class="p-desc"> Description: ' + data[key].description + '</p>';
                htmlText += '<p class="p-created"> Created by: ' + data[key].created_by + '</p>';
                htmlText += '<p class="p-uname"> Username: ' + data[key].users_name + '</p>';
                htmlText += '</div>';
            }

            $('body').append(htmlText);