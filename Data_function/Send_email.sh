#!/bin/bash 
 
## declare mail variables
##email subject 
subject="Running Status actualization"
##sending mail as
from="ssh ffwng@domino.ucr.edu"
## sending mail to
to="nataliaopzc@gmail.com"
## send carbon copy to
also_to="neopazo@uc.cl"


 ## send email if experiment is running
echo "Your experiment $1 is running now!. Greetings :)." 

exit 0
