#!/bin/bash

FOOT="/home/dhenn/.config/foot"

case $3 in
	night)
	    cp $FOOT/themes/modus-vivendi.ini $FOOT/themes/current.ini;;
	
	daytime)
	    cp $FOOT/themes/modus-operandi.ini $FOOT/themes/current.ini;;
esac


