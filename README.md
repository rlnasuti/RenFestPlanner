# RenFestPlanner
A bot that will look at a Renaissance Festival flyer and generate an itinerary for the user

To run:

1. install required libraries from requirements.txt
1. create a file in the root of this repo called `.env`
1. populate required fields in .env
```
OPENAI_API_KEY="<your openai api key"
PDF_FILE_PATH="location of Renaissance Faire program pdf on your computer"
```

Example run:
```
Greetings, mine gentle traveler. As ye requested, here is thine itinerary for anon fair journey to ye Colorado Renaissance Festival on 6/31/23:

1. Arriveth promptly at 10:30 am at the festinval to maketh the most of what doth await.
2. Advance to Leoanardo Da Vinci Ride for mirth and exhilarance at 11:00 am.
3. Graceth thine presence upon the Tournament of Skill at the Joust Arena at 11:30 am to witnesse the knights of Noble Cause Productions in combat.
4. Hie thee to ye Fortune Stage at 12:30 pm for London Broil's truly remarkable display of juggling antics.
5. Break thy fast, indulge thyself at ye International Food Court at 1:00 pm, partaking in variegated sustenance.
6. Attend the Royal Procession at 1:30 pm to gaze upon the resplendent court's gallant march.
7. Saunter o'er to the Pirate Ship Stage at 2:30 pm for jocund wit and entertaining tales from Zilch, the Torysteller.
8. At 3:30 pm, visit ye Celestial Stage for an enchanting spectacle of Chaste Treasure's harmonious melodies.
9. Be a partaker in the Knighting Ceremony at Canterbury Chapel at 3:45 pm to experience joyous customs of olde.
10. Arrive at ye Joust Arena for the Tournament of Arms at 4:30 pm, further feats of strenuous strife 'twixt brave knights.
11. At 5:30 pm, caper to ye Beer and Soda booth to slake thy thirst with thirst-quenching beverages fit for nobles.
12. Finally, at 6:00 pm, attend the Pub Sing at the Celestial Stage for a convivial denouement to thine adventurous day.

Fare thee well on thy mirthful journey, and may favorable fortune be thy companioneth!
```