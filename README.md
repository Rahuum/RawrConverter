# RawrConverter

Allows you to generate Rawr 3.3.5 character XML files from your ElitistGroups addon's SavedVariables.

To use:
1. run ./rawrconverter
2. When prompted, provide the path to your wow install and the account that has the savedvariables. (RawrConverter will save this information locally in the same folder so you won't be prompted again)
3. You will be given a list of character names that RawrConverter has found in your savedvariables.
4. Type in the character name.
5. Your character XML has been generated.
6. Open Rawr.
7. In rawr, open the character file generated in step 5.
8. In rawr, ensure that your 'model' in the top left is correct (we may not pick up feral druids properly)
9. Go to the top tab bar, select Talents, and choose the appropriate talents and glyphs (We cannot pick up your actual talents beyond how many points are in each tree.)
10. In the top menu bar, go to 'Tools' -> 'Optimize' and press 'Optimize' on the popup. This may take a while.
11. Results will be on the left, with an 'at a glance' summary in the bottom left.
