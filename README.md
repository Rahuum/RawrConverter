# RawrConverter

Allows you to generate Rawr 3.3.5 character XML files from your ElitistGroups addon's SavedVariables.
ElitistGroups for 3.3.5 can be found at [WoWAce](https://www.wowace.com/projects/elitistgroup/files/445209).

To use:
1. Run `python3 rawrconverter.py`
2. When prompted, provide the path to your WoW 3.3.5 install and the account name that has ElitistGroups enabled. (RawrConverter will save this information locally in the same folder so you won't be prompted again.)
3. You will be given a list of character names that RawrConverter has found in your SavedVariables.
4. Input the character name you want a Rawr profile for.
5. Your character XML has been generated.
6. Open Rawr.
7. In Rawr, open the character file generated in step 5.
8. Ensure that your 'model' in the top left is correct (Feral druids may not be picked up properly because EG does not supply full talent information.)
9. If you wish, you should set your professions and ensure your race is correct. (EG does not supply this information either.)
9. Go to the top tab bar, select Talents, and choose the appropriate specialization and glyphs.
10. In the top menu bar, go to 'Tools' -> 'Optimize' and press 'Optimize' on the popup. This may take a while.
11. Results will be on the left, with an 'at a glance' summary in the bottom left.
