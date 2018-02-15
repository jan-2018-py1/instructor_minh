# Activity for week 2 session 2
Purpose of activity - Create a rock paper scissor game. The user gets to decide his choice and the computer choice is randomize. 

Application should have 2 routes - 

routes - "/rockpaperscissor" - page with statistics of user wins vs computer wins vs draws. Page should also have a form where user can select rock paper or scissor(using a check box or select tag) AND 3 links that allows user to click rock paper or scissor. This allows user to play by selecting the link OR submitting the form. The form submission should go to "/rockpaperscissor/form". 

routes - "/rockpaperscissor/<choice>" - play rock paper scissor with the computer. Let the computer chose randomly(random int), calculate who wins(Possibly lots of if statements here), tally up the score and redirect to index to display score. 
