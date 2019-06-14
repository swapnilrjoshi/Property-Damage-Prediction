# Property Damage Prediction
Predict property damage from an ensuring weather event, so that the insurance company can hold on writing new insurance policies in that area

# Data
The dataset is taken from [NOAA](https://www.noaa.gov/) and contains information on all storms in the US since 2006.

Fields of interest are:
-id: The event identifier.
-BLat: The beginning latitude of the event/storm.
-BLon: The beginning longitude of the event/storm.
-ELat: The ending latitude of the event/storm.
-ELon: The ending longitude of the event/storm.
Please note: Storm Data has gone through many changes and versions over the years. The source data ingested into the database are widely varied and leads to many questions about the precision and accuracy of the location data.
-Report Source: The source that reported the event.
-Magnitude: Represents the magnitude of the event/storm.
When listing hail size under Magnitude (e.g., 2.25 in.), the hail size is given in inches and hundredths of inches.
When listing wind speed values under Magnitude (e.g., 81 kts.), the value listed is can be either estimated by damage caused, or measured by official NWS approved calibrated anemometers. 1 kt. = 1.152 mph. (Measures Gust, Measured Sustained, Estimated Gust or Estimated Sustained)
-Injuries Direct/Indirect: The injuries reported from the event.
-Deaths Direct/Indirect: The deaths reported from the event.
-Event Narrative: The event narrative provides more specific details of the individual event . The event narrative is provided by NWS. A message sent out to the public about the specific event.
-Event: An Event is an individual type of storm event.
-Episode Narrative: An Episode is an entire storm system and can contain many different types of events. The episode narrative depicts the general nature and overall activity of the episode, created by NWS. A message to the public about the surrounding event(s).
-Rainfall: Reported total rainfall that occurred during the event.
-Windspeed: Reported average wind speed during the event.
-IsPropertyDamage: If property damage resulted from the event.

For more information on data check:https://www.ncdc.noaa.gov/stormevents/faq.jsp
