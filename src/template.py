﻿template = """<?xml version="1.0" encoding="utf-8"?>
<Character xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <Name>{name}</Name>
  <Realm>Algalon</Realm>
  <Region>US</Region>
  <Race>{race}</Race>
  <Class>{class_name}</Class>
{available}
  <ActiveBuffs>Blessing of Sanctuary</ActiveBuffs>
  <ActiveBuffs>Blessing of Sanctuary (Str/Sta Bonus)</ActiveBuffs>
  <ActiveBuffs>Blessing of Kings</ActiveBuffs>
  <ActiveBuffs>Blessing of Kings (Str/Sta Bonus)</ActiveBuffs>
  <ActiveBuffs>Strength of Earth Totem</ActiveBuffs>
  <ActiveBuffs>Ancestral Healing</ActiveBuffs>
  <ActiveBuffs>Blessing of Might</ActiveBuffs>
  <ActiveBuffs>Improved Blessing of Might</ActiveBuffs>
  <ActiveBuffs>Ferocious Inspiration</ActiveBuffs>
  <ActiveBuffs>Swift Retribution</ActiveBuffs>
  <ActiveBuffs>Commanding Shout</ActiveBuffs>
  <ActiveBuffs>Commanding Presence (Health)</ActiveBuffs>
  <ActiveBuffs>Arcane Intellect</ActiveBuffs>
  <ActiveBuffs>Leader of the Pack</ActiveBuffs>
  <ActiveBuffs>Improved Leader of the Pack</ActiveBuffs>
  <ActiveBuffs>Judgements of the Wise</ActiveBuffs>
  <ActiveBuffs>Blessing of Wisdom</ActiveBuffs>
  <ActiveBuffs>Improved Blessing of Wisdom</ActiveBuffs>
  <ActiveBuffs>Power Word: Fortitude</ActiveBuffs>
  <ActiveBuffs>Improved Power Word: Fortitude</ActiveBuffs>
  <ActiveBuffs>Mark of the Wild</ActiveBuffs>
  <ActiveBuffs>Improved Mark of the Wild</ActiveBuffs>
  <ActiveBuffs>Sunder Armor</ActiveBuffs>
  <ActiveBuffs>Faerie Fire</ActiveBuffs>
  <ActiveBuffs>Mangle</ActiveBuffs>
  <ActiveBuffs>Heart of the Crusader</ActiveBuffs>
  <ActiveBuffs>Judgement of Wisdom</ActiveBuffs>
  <ActiveBuffs>Blood Frenzy</ActiveBuffs>
  <ActiveBuffs>Earth and Moon</ActiveBuffs>
  <ActiveBuffs>Flask of Endless Rage</ActiveBuffs>
  <ActiveBuffs>Fish Feast</ActiveBuffs>
  <ActiveBuffs>Trueshot Aura</ActiveBuffs>
  <ActiveBuffs>Hunter's Mark</ActiveBuffs>
  <ActiveBuffs>Improved and Glyphed Hunter's Mark</ActiveBuffs>
  <CurrentModel>{model}</CurrentModel>
  <EnforceMetagemRequirements>true</EnforceMetagemRequirements>
  <CalculationOptions>
    <item>
      <key>
        <string>Bear</string>
      </key>
      <value>
        <string>&lt;?xml version="1.0" encoding="utf-16"?&gt;
&lt;CalculationOptionsBear xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"&gt;
  &lt;ThreatScale&gt;10&lt;/ThreatScale&gt;
  &lt;SurvivalSoftCap&gt;160000&lt;/SurvivalSoftCap&gt;
  &lt;TemporarySurvivalScale&gt;1&lt;/TemporarySurvivalScale&gt;
  &lt;TargetLevel&gt;83&lt;/TargetLevel&gt;
  &lt;TargetArmor&gt;10643&lt;/TargetArmor&gt;
  &lt;TargetDamage&gt;65000&lt;/TargetDamage&gt;
  &lt;TargetAttackSpeed&gt;2&lt;/TargetAttackSpeed&gt;
  &lt;TargetParryHastes&gt;true&lt;/TargetParryHastes&gt;
  &lt;CustomUseMaul&gt;false&lt;/CustomUseMaul&gt;
  &lt;CustomUseMangle&gt;false&lt;/CustomUseMangle&gt;
  &lt;CustomUseSwipe&gt;false&lt;/CustomUseSwipe&gt;
  &lt;CustomUseFaerieFire&gt;false&lt;/CustomUseFaerieFire&gt;
  &lt;CustomUseLacerate&gt;false&lt;/CustomUseLacerate&gt;
&lt;/CalculationOptionsBear&gt;</string>
      </value>
    </item>
    <item>
      <key>
        <string>Hunter</string>
      </key>
      <value>
        <string>&lt;?xml version="1.0" encoding="utf-16"?&gt;
&lt;CalculationOptionsHunter xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"&gt;
  &lt;_TimeSpentSub20&gt;72&lt;/_TimeSpentSub20&gt;
  &lt;_TimeSpent35To20&gt;54&lt;/_TimeSpent35To20&gt;
  &lt;_BossHPPerc&gt;1&lt;/_BossHPPerc&gt;
  &lt;_CDCutoff&gt;0&lt;/_CDCutoff&gt;
  &lt;_AspectUsage&gt;ViperToOOM&lt;/_AspectUsage&gt;
  &lt;_UseBeastDuringBestialWrath&gt;true&lt;/_UseBeastDuringBestialWrath&gt;
  &lt;_UseRotationTest&gt;true&lt;/_UseRotationTest&gt;
  &lt;_RandomizeProcs&gt;false&lt;/_RandomizeProcs&gt;
  &lt;_PriorityIndex1&gt;0&lt;/_PriorityIndex1&gt;
  &lt;_PriorityIndex2&gt;0&lt;/_PriorityIndex2&gt;
  &lt;_PriorityIndex3&gt;0&lt;/_PriorityIndex3&gt;
  &lt;_PriorityIndex4&gt;0&lt;/_PriorityIndex4&gt;
  &lt;_PriorityIndex5&gt;0&lt;/_PriorityIndex5&gt;
  &lt;_PriorityIndex6&gt;0&lt;/_PriorityIndex6&gt;
  &lt;_PriorityIndex7&gt;0&lt;/_PriorityIndex7&gt;
  &lt;_PriorityIndex8&gt;0&lt;/_PriorityIndex8&gt;
  &lt;_PriorityIndex9&gt;0&lt;/_PriorityIndex9&gt;
  &lt;_PriorityIndex10&gt;0&lt;/_PriorityIndex10&gt;
  &lt;_PetPriority1&gt;Growl&lt;/_PetPriority1&gt;
  &lt;_PetPriority2&gt;Bite&lt;/_PetPriority2&gt;
  &lt;_PetPriority3&gt;None&lt;/_PetPriority3&gt;
  &lt;_PetPriority4&gt;None&lt;/_PetPriority4&gt;
  &lt;_PetPriority5&gt;None&lt;/_PetPriority5&gt;
  &lt;_PetPriority6&gt;None&lt;/_PetPriority6&gt;
  &lt;_PetPriority7&gt;None&lt;/_PetPriority7&gt;
  &lt;waitForCooldown&gt;0.8&lt;/waitForCooldown&gt;
  &lt;interleaveLAL&gt;false&lt;/interleaveLAL&gt;
  &lt;prioritiseArcAimedOverSteady&gt;true&lt;/prioritiseArcAimedOverSteady&gt;
  &lt;debugShotRotation&gt;false&lt;/debugShotRotation&gt;
  &lt;TargetLevel&gt;83&lt;/TargetLevel&gt;
  &lt;TargetArmor&gt;10643&lt;/TargetArmor&gt;
  &lt;Duration&gt;300&lt;/Duration&gt;
  &lt;TimeSpentSub20&gt;72&lt;/TimeSpentSub20&gt;
  &lt;TimeSpent35To20&gt;54&lt;/TimeSpent35To20&gt;
  &lt;MultipleTargets&gt;false&lt;/MultipleTargets&gt;
  &lt;MultipleTargetsPerc&gt;0&lt;/MultipleTargetsPerc&gt;
  &lt;Lag&gt;150&lt;/Lag&gt;
  &lt;React&gt;200&lt;/React&gt;
  &lt;BossHPPerc&gt;1&lt;/BossHPPerc&gt;
  &lt;CDCutoff&gt;0&lt;/CDCutoff&gt;
  &lt;SelectedAspect&gt;Dragonhawk&lt;/SelectedAspect&gt;
  &lt;AspectUsage&gt;ViperToOOM&lt;/AspectUsage&gt;
  &lt;UseBeastDuringBestialWrath&gt;true&lt;/UseBeastDuringBestialWrath&gt;
  &lt;UseRotationTest&gt;true&lt;/UseRotationTest&gt;
  &lt;RandomizeProcs&gt;false&lt;/RandomizeProcs&gt;
  &lt;PriorityIndex1&gt;0&lt;/PriorityIndex1&gt;
  &lt;PriorityIndex2&gt;0&lt;/PriorityIndex2&gt;
  &lt;PriorityIndex3&gt;0&lt;/PriorityIndex3&gt;
  &lt;PriorityIndex4&gt;0&lt;/PriorityIndex4&gt;
  &lt;PriorityIndex5&gt;0&lt;/PriorityIndex5&gt;
  &lt;PriorityIndex6&gt;0&lt;/PriorityIndex6&gt;
  &lt;PriorityIndex7&gt;0&lt;/PriorityIndex7&gt;
  &lt;PriorityIndex8&gt;0&lt;/PriorityIndex8&gt;
  &lt;PriorityIndex9&gt;0&lt;/PriorityIndex9&gt;
  &lt;PriorityIndex10&gt;0&lt;/PriorityIndex10&gt;
  &lt;PetLevel&gt;80&lt;/PetLevel&gt;
  &lt;SelectedArmoryPet&gt;0&lt;/SelectedArmoryPet&gt;
  &lt;PetHappinessLevel&gt;Happy&lt;/PetHappinessLevel&gt;
  &lt;petTalents&gt;0000000000000000000000000000000000000&lt;/petTalents&gt;
  &lt;PetFamily&gt;Cat&lt;/PetFamily&gt;
  &lt;PetPriority1&gt;Growl&lt;/PetPriority1&gt;
  &lt;PetPriority2&gt;Bite&lt;/PetPriority2&gt;
  &lt;PetPriority3&gt;None&lt;/PetPriority3&gt;
  &lt;PetPriority4&gt;None&lt;/PetPriority4&gt;
  &lt;PetPriority5&gt;None&lt;/PetPriority5&gt;
  &lt;PetPriority6&gt;None&lt;/PetPriority6&gt;
  &lt;PetPriority7&gt;None&lt;/PetPriority7&gt;
  &lt;HideBadItems_Spl&gt;true&lt;/HideBadItems_Spl&gt;
  &lt;HideBadItems_PvP&gt;true&lt;/HideBadItems_PvP&gt;
  &lt;PTRMode&gt;false&lt;/PTRMode&gt;
  &lt;SurvScale&gt;1&lt;/SurvScale&gt;
  &lt;SE_UseDur&gt;true&lt;/SE_UseDur&gt;
  &lt;StatsList&gt;
    &lt;boolean&gt;true&lt;/boolean&gt;
    &lt;boolean&gt;true&lt;/boolean&gt;
    &lt;boolean&gt;true&lt;/boolean&gt;
    &lt;boolean&gt;true&lt;/boolean&gt;
    &lt;boolean&gt;true&lt;/boolean&gt;
    &lt;boolean&gt;true&lt;/boolean&gt;
  &lt;/StatsList&gt;
  &lt;StatsIncrement&gt;100&lt;/StatsIncrement&gt;
  &lt;CalculationToGraph&gt;Overall Rating&lt;/CalculationToGraph&gt;
  &lt;useKillCommand&gt;true&lt;/useKillCommand&gt;
  &lt;gcdsToLayImmoTrap&gt;2&lt;/gcdsToLayImmoTrap&gt;
  &lt;gcdsToLayExploTrap&gt;2&lt;/gcdsToLayExploTrap&gt;
  &lt;gcdsToVolley&gt;4&lt;/gcdsToVolley&gt;
  &lt;LALShotToUse&gt;ExplosiveShot&lt;/LALShotToUse&gt;
  &lt;LALShotsReplaced&gt;2&lt;/LALShotsReplaced&gt;
  &lt;LALProcChance&gt;2&lt;/LALProcChance&gt;
&lt;/CalculationOptionsHunter&gt;</string>
      </value>
    </item>
  </CalculationOptions>
{equipment}
  <CustomGemmingTemplates />
  <GemmingTemplateOverrides />
  <ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Dungeons</Name>
      <Enabled>false</Enabled>
      <SubFilterOverride>
        <ItemFilterEnabledOverride>
          <Name>Ahn'kahet</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Azjol-Nerub</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>The Culling of Stratholme</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Drak'Tharon Keep</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Forge of Souls</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Gundrak</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Halls of Lightning</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Halls of Stone</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Halls of Reflection</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Nexus</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Pit of Saron</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>The Oculus</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Trial of the Champion</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Utgarde Keep</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Utgarde Pinnacle</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Violet Hold</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Other</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
      </SubFilterOverride>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Dungeons (Heroic)</Name>
      <Enabled>false</Enabled>
      <SubFilterOverride>
        <ItemFilterEnabledOverride>
          <Name>Ahn'kahet</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Azjol-Nerub</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>The Culling of Stratholme</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Drak'Tharon Keep</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Forge of Souls</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Gundrak</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Halls of Lightning</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Halls of Stone</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Halls of Reflection</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Nexus</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Pit of Saron</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>The Oculus</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Trial of the Champion</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Utgarde Keep</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Utgarde Pinnacle</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Violet Hold</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Other</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
      </SubFilterOverride>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Tier 7 Raids (10/25) Nax/EoE/OS</Name>
      <Enabled>false</Enabled>
      <SubFilterOverride>
        <ItemFilterEnabledOverride>
          <Name>10 Man Raids</Name>
          <Enabled>false</Enabled>
          <SubFilterOverride>
            <ItemFilterEnabledOverride>
              <Name>Naxxramas</Name>
              <Enabled>false</Enabled>
              <SubFilterOverride>
                <ItemFilterEnabledOverride>
                  <Name>Construct Quarter</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Patchwerk</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Grobbulus</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Gluth</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Thaddius</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Plague Quarter</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Noth the Plaguebringer</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Heigan the Unclean</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Loatheb</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Spider Quarter</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Anub'Rekhan</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Grand Widow Faerlina</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Maexxna</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Military Quarter</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Instructor Razuvious</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Gothik the Harvester</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>The Four Horsemen</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Frostwyrm Lair</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Sapphiron</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Kel'Thuzad</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Trash Drops</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Other</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
              </SubFilterOverride>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Eye of Eternity</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Obsidian Sanctum</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Other</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
          </SubFilterOverride>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>25 Man Raids</Name>
          <Enabled>false</Enabled>
          <SubFilterOverride>
            <ItemFilterEnabledOverride>
              <Name>Naxxramas</Name>
              <Enabled>false</Enabled>
              <SubFilterOverride>
                <ItemFilterEnabledOverride>
                  <Name>Construct Quarter</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Patchwerk</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Grobbulus</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Gluth</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Thaddius</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Plague Quarter</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Noth the Plaguebringer</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Heigan the Unclean</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Loatheb</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Spider Quarter</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Anub'Rekhan</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Grand Widow Faerlina</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Maexxna</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Military Quarter</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Instructor Razuvious</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Gothik the Harvester</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>The Four Horsemen</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Frostwyrm Lair</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Sapphiron</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Kel'Thuzad</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Trash Drops</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Other</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
              </SubFilterOverride>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Eye of Eternity</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Obsidian Sanctum</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Other</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
          </SubFilterOverride>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Other</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
      </SubFilterOverride>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Tier 8 Raids (10/25) ULD</Name>
      <Enabled>false</Enabled>
      <SubFilterOverride>
        <ItemFilterEnabledOverride>
          <Name>Ulduar (10)</Name>
          <Enabled>false</Enabled>
          <SubFilterOverride>
            <ItemFilterEnabledOverride>
              <Name>Flame Leviathan</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Ignis the Furnace Master</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Razorscale</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>XT-002 Deconstructor</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Assembly of Iron</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Kologarn</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Auriaya</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Mimiron</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Hodir</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Thorim</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Freya</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>General Vezax</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Yogg-Saron</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Algalon the Observer</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Quest Rewards</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Trash</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Other</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
          </SubFilterOverride>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Ulduar (25)</Name>
          <Enabled>false</Enabled>
          <SubFilterOverride>
            <ItemFilterEnabledOverride>
              <Name>Flame Leviathan</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Ignis the Furnace Master</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Razorscale</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>XT-002 Deconstructor</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Assembly of Iron</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Kologarn</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Auriaya</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Mimiron</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Hodir</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Thorim</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Freya</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>General Vezax</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Yogg-Saron</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Algalon the Observer</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Quest Rewards</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Trash</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Other</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
          </SubFilterOverride>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Other</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
      </SubFilterOverride>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Tier 9 Raids (10/25) ToC/ToGC</Name>
      <Enabled>false</Enabled>
      <SubFilterOverride>
        <ItemFilterEnabledOverride>
          <Name>10 Man Raids</Name>
          <Enabled>false</Enabled>
          <SubFilterOverride>
            <ItemFilterEnabledOverride>
              <Name>Trial of the Crusader</Name>
              <Enabled>false</Enabled>
              <SubFilterOverride>
                <ItemFilterEnabledOverride>
                  <Name>Northrend Beasts</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Lord Jaraxxus</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Faction Champions</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Twin Val'kyr</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Anub'arak</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Other</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
              </SubFilterOverride>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Trial of the Grand Crusader</Name>
              <Enabled>false</Enabled>
              <SubFilterOverride>
                <ItemFilterEnabledOverride>
                  <Name>Northrend Beasts</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Lord Jaraxxus</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Faction Champions</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Twin Val'kyr</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Anub'arak</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Tribute Chest</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Other</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
              </SubFilterOverride>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Other</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
          </SubFilterOverride>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>25 Man Raids</Name>
          <Enabled>false</Enabled>
          <SubFilterOverride>
            <ItemFilterEnabledOverride>
              <Name>Trial of the Crusader</Name>
              <Enabled>false</Enabled>
              <SubFilterOverride>
                <ItemFilterEnabledOverride>
                  <Name>Northrend Beasts</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Lord Jaraxxus</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Faction Champions</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Twin Val'kyr</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Anub'arak</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Other</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
              </SubFilterOverride>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Trial of the Grand Crusader</Name>
              <Enabled>false</Enabled>
              <SubFilterOverride>
                <ItemFilterEnabledOverride>
                  <Name>Northrend Beasts</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Lord Jaraxxus</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Faction Champions</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Twin Val'kyr</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Anub'arak</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Tribute Chest</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Other</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
              </SubFilterOverride>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Other</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
          </SubFilterOverride>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Other</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
      </SubFilterOverride>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Tier 10 Raids (10/25) ICC</Name>
      <Enabled>true</Enabled>
      <SubFilterOverride>
        <ItemFilterEnabledOverride>
          <Name>Icecrown Citadel (10)</Name>
          <Enabled>true</Enabled>
          <SubFilterOverride>
            <ItemFilterEnabledOverride>
              <Name>Normal</Name>
              <Enabled>true</Enabled>
              <SubFilterOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Lower Spire</Name>
                  <Enabled>true</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Lord Marrowgar</Name>
                      <Enabled>true</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Lady Deathwhisper</Name>
                      <Enabled>true</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Gunship Battle</Name>
                      <Enabled>true</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Deathbringer Saurfang</Name>
                      <Enabled>true</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>true</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Plagueworks</Name>
                  <Enabled>true</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Festergut</Name>
                      <Enabled>true</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Rotface</Name>
                      <Enabled>true</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Professor Putricide</Name>
                      <Enabled>true</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>true</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Crimson Hall</Name>
                  <Enabled>true</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Blood Prince Council</Name>
                      <Enabled>true</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Blood-Queen Lana'thel</Name>
                      <Enabled>true</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>true</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Frostwing Hall</Name>
                  <Enabled>true</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Valithria Dreamwalker</Name>
                      <Enabled>true</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Sindragosa</Name>
                      <Enabled>true</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>true</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Frozen Throne</Name>
                  <Enabled>true</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>The Lich King</Name>
                      <Enabled>true</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>true</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Other</Name>
                  <Enabled>true</Enabled>
                </ItemFilterEnabledOverride>
              </SubFilterOverride>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Heroic</Name>
              <Enabled>false</Enabled>
              <SubFilterOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Lower Spire</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Lord Marrowgar</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Lady Deathwhisper</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Gunship Battle</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Deathbringer Saurfang</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Plagueworks</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Festergut</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Rotface</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Professor Putricide</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Crimson Hall</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Blood Prince Council</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Blood-Queen Lana'thel</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Frostwing Hall</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Valithria Dreamwalker</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Sindragosa</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Frozen Throne</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>The Lich King</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Other</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
              </SubFilterOverride>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Other</Name>
              <Enabled>true</Enabled>
            </ItemFilterEnabledOverride>
          </SubFilterOverride>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Icecrown Citadel (25)</Name>
          <Enabled>false</Enabled>
          <SubFilterOverride>
            <ItemFilterEnabledOverride>
              <Name>Normal</Name>
              <Enabled>false</Enabled>
              <SubFilterOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Lower Spire</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Lord Marrowgar</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Lady Deathwhisper</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Gunship Battle</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Deathbringer Saurfang</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Plagueworks</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Festergut</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Rotface</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Professor Putricide</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Crimson Hall</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Blood Prince Council</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Blood-Queen Lana'thel</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Frostwing Hall</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Valithria Dreamwalker</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Sindragosa</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Frozen Throne</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>The Lich King</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Other</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
              </SubFilterOverride>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Heroic</Name>
              <Enabled>false</Enabled>
              <SubFilterOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Lower Spire</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Lord Marrowgar</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Lady Deathwhisper</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Gunship Battle</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Deathbringer Saurfang</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Plagueworks</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Festergut</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Rotface</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Professor Putricide</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Crimson Hall</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Blood Prince Council</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Blood-Queen Lana'thel</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Frostwing Hall</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Valithria Dreamwalker</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Sindragosa</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>The Frozen Throne</Name>
                  <Enabled>false</Enabled>
                  <SubFilterOverride>
                    <ItemFilterEnabledOverride>
                      <Name>The Lich King</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                    <ItemFilterEnabledOverride>
                      <Name>Other</Name>
                      <Enabled>false</Enabled>
                    </ItemFilterEnabledOverride>
                  </SubFilterOverride>
                </ItemFilterEnabledOverride>
                <ItemFilterEnabledOverride>
                  <Name>Other</Name>
                  <Enabled>false</Enabled>
                </ItemFilterEnabledOverride>
              </SubFilterOverride>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Other</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
          </SubFilterOverride>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Rewards</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Trash</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Other</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
      </SubFilterOverride>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Vault of Archavon (10/25)</Name>
      <Enabled>false</Enabled>
      <SubFilterOverride>
        <ItemFilterEnabledOverride>
          <Name>10 Man Raids</Name>
          <Enabled>false</Enabled>
          <SubFilterOverride>
            <ItemFilterEnabledOverride>
              <Name>Archavon the Stone Watcher</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Emalon the Storm Watcher</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Koralon the Flame Watcher</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Toravon the Ice Watcher</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Other</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
          </SubFilterOverride>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>25 Man Raids</Name>
          <Enabled>false</Enabled>
          <SubFilterOverride>
            <ItemFilterEnabledOverride>
              <Name>Archavon the Stone Watcher</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Emalon the Storm Watcher</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Koralon the Flame Watcher</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Toravon the Ice Watcher</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Other</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
          </SubFilterOverride>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Other</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
      </SubFilterOverride>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Onyxia's Lair (10/25)</Name>
      <Enabled>false</Enabled>
      <SubFilterOverride>
        <ItemFilterEnabledOverride>
          <Name>Onyxia's Lair (10)</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Onyxia's Lair (25)</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Other</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
      </SubFilterOverride>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Ruby Sanctum (10/25)</Name>
      <Enabled>false</Enabled>
      <SubFilterOverride>
        <ItemFilterEnabledOverride>
          <Name>Ruby Sanctum (10)</Name>
          <Enabled>false</Enabled>
          <SubFilterOverride>
            <ItemFilterEnabledOverride>
              <Name>Normal</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Heroic</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Other</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
          </SubFilterOverride>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Ruby Sanctum (25)</Name>
          <Enabled>false</Enabled>
          <SubFilterOverride>
            <ItemFilterEnabledOverride>
              <Name>Normal</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Heroic</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Other</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
          </SubFilterOverride>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Other</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
      </SubFilterOverride>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Special Currency (Emblems, Tokens, etc.)</Name>
      <Enabled>true</Enabled>
      <SubFilterOverride>
        <ItemFilterEnabledOverride>
          <Name>Badge of Justice</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Venture Coin</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Mark of Honor</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Stone Keeper's Shard</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Emblem of Heroism</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Emblem of Valor</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Emblem of Conquest</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Emblem of Triumph</Name>
          <Enabled>true</Enabled>
          <SubFilterOverride>
            <ItemFilterEnabledOverride>
              <Name>Emblem of Triumph</Name>
              <Enabled>true</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Trophy of the Crusade</Name>
              <Enabled>true</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Other</Name>
              <Enabled>true</Enabled>
            </ItemFilterEnabledOverride>
          </SubFilterOverride>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Emblem of Frost</Name>
          <Enabled>true</Enabled>
          <SubFilterOverride>
            <ItemFilterEnabledOverride>
              <Name>Emblem of Frost</Name>
              <Enabled>true</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Class Token</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Other</Name>
              <Enabled>true</Enabled>
            </ItemFilterEnabledOverride>
          </SubFilterOverride>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Champion's Seal</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Kirin Tor Rings</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Armor Tokens</Name>
          <Enabled>false</Enabled>
          <SubFilterOverride>
            <ItemFilterEnabledOverride>
              <Name>Tier 7</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Tier 8</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Tier 9</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Tier 10</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
            <ItemFilterEnabledOverride>
              <Name>Other</Name>
              <Enabled>false</Enabled>
            </ItemFilterEnabledOverride>
          </SubFilterOverride>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Other</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
      </SubFilterOverride>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Crafted</Name>
      <Enabled>true</Enabled>
      <SubFilterOverride>
        <ItemFilterEnabledOverride>
          <Name>Alchemy</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Blacksmithing</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Engineer</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Inscription</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Jewelcrafting (non-gem)</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Leatherworking</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Tailoring</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>? (Refresh from Wowhead)</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Other</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
      </SubFilterOverride>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Faction Reputation</Name>
      <Enabled>true</Enabled>
      <SubFilterOverride>
        <ItemFilterEnabledOverride>
          <Name>Alliance Vanguard</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Argent Crusade</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Frenzyheart Tribe</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Horde Expedition</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Kalu'ak</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Kirin Tor</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Knights of the Ebon Blade</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>The Oracles</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>The Sons of Hodir</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Wyrmrest Accord</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Misc. Vendor</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Other</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
      </SubFilterOverride>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Rare Elite</Name>
      <Enabled>false</Enabled>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>PvP</Name>
      <Enabled>false</Enabled>
      <SubFilterOverride>
        <ItemFilterEnabledOverride>
          <Name>Requires Arena Rating</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Arena Points</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Honor Points</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Mark of Honor</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Emblem of Valor</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Emblem of Heroism</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Emblem of Conquest</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>? (Refresh from Armory)</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Other</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
      </SubFilterOverride>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Quest Rewards</Name>
      <Enabled>false</Enabled>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>World Drop</Name>
      <Enabled>true</Enabled>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Burning Crusade</Name>
      <Enabled>false</Enabled>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Classic</Name>
      <Enabled>false</Enabled>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Seasonal</Name>
      <Enabled>true</Enabled>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Unknown/Not found on armory</Name>
      <Enabled>false</Enabled>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Disable Gems</Name>
      <Enabled>false</Enabled>
      <SubFilterOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable Jewelcrafter BoP</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable Crafted (Non-BoP)</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable PvP</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable World Drop</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable Quest Rewards</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable Unknown/Not found on armory</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Other</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
      </SubFilterOverride>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Disable BoP Crafted</Name>
      <Enabled>true</Enabled>
      <SubFilterOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable BoP Alchemy</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable BoP Blacksmithing</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable BoP Engineering</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable BoP Inscription</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable BoP Jewelcrafting (non-gem)</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable BoP Leatherworking</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable BoP Tailoring</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Other</Name>
          <Enabled>true</Enabled>
        </ItemFilterEnabledOverride>
      </SubFilterOverride>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Disable by Item Level</Name>
      <Enabled>false</Enabled>
      <SubFilterOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable 0-1 (Heirloom)</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable 2-199     Tier 1-6</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable 200-218 Tier 7</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable 219-231 Tier 8</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable 232-250 Tier 9</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable 251-276 Tier 10</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable 277</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Disable 278+</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Other</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
      </SubFilterOverride>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Disable by Bind Type</Name>
      <Enabled>false</Enabled>
      <SubFilterOverride>
        <ItemFilterEnabledOverride>
          <Name>Binds on Pickup</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Binds on Account</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Binds on Equip</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Binds on Use</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
        <ItemFilterEnabledOverride>
          <Name>Other</Name>
          <Enabled>false</Enabled>
        </ItemFilterEnabledOverride>
      </SubFilterOverride>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>BOE Items (possible AH)</Name>
      <Enabled>false</Enabled>
    </ItemFilterEnabledOverride>
    <ItemFilterEnabledOverride>
      <Name>Other</Name>
      <Enabled>false</Enabled>
    </ItemFilterEnabledOverride>
  </ItemFilterEnabledOverride>
  <Boss>
    <Targets />
    <Moves />
    <Stuns />
    <Fears />
    <Roots />
    <Disarms />
    <Name>Generic</Name>
    <Content>T7_0</Content>
    <Instance>None</Instance>
    <Version>V_10N</Version>
    <Comment>No comments have been written for this Boss.</Comment>
    <Level>83</Level>
    <Armor>10643</Armor>
    <BerserkTimer>480</BerserkTimer>
    <SpeedKillTimer>180</SpeedKillTimer>
    <Health>1000000</Health>
    <InBackPerc_Melee>0</InBackPerc_Melee>
    <InBackPerc_Ranged>0</InBackPerc_Ranged>
    <Max_Players>10</Max_Players>
    <Min_Healers>3</Min_Healers>
    <Min_Tanks>2</Min_Tanks>
    <DoTs />
    <Attacks />
    <Resist_Physical>0</Resist_Physical>
    <Resist_Frost>0</Resist_Frost>
    <Resist_Fire>0</Resist_Fire>
    <Resist_Nature>0</Resist_Nature>
    <Resist_Arcane>0</Resist_Arcane>
    <Resist_Shadow>0</Resist_Shadow>
    <Resist_Holy>0</Resist_Holy>
    <TimeBossIsInvuln>0</TimeBossIsInvuln>
    <InBack>false</InBack>
    <MultiTargs>false</MultiTargs>
    <StunningTargs>false</StunningTargs>
    <MovingTargs>false</MovingTargs>
    <FearingTargs>false</FearingTargs>
    <RootingTargs>false</RootingTargs>
    <DisarmingTargs>false</DisarmingTargs>
    <DamagingTargs>false</DamagingTargs>
    <Under35Perc>0.1</Under35Perc>
    <Under20Perc>0.15</Under20Perc>
    <FilterType>Content</FilterType>
    <Filter />
    <BossName />
  </Boss>
  <WarriorTalents>0000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0000000000000000000000000000000000</WarriorTalents>
  <PaladinTalents>000000000000000000000000000000000000000000000000000000000000000000000000000000.0000000000000000000000000000000000</PaladinTalents>
  <HunterTalents>000000000000000000000000000000000000000000000000000000000000000000000000000000000.000000000000000000000000000000000</HunterTalents>
  <RogueTalents>00000000000000000000000000000000000000000000000000000000000000000000000000000000000.0000000000000000000000000000000000</RogueTalents>
  <PriestTalents>0000000000000000000000000000000000000000000000000000000000000000000000000000000000.000000000000000000000000000000000</PriestTalents>
  <ShamanTalents>00000000000000000000000000000000000000000000000000000000000000000000000000000000.00000000000000000000000000000</ShamanTalents>
  <MageTalents>00000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0000000000000000000</MageTalents>
  <WarlockTalents>000000000000000000000000000000000000000000000000000000000000000000000000000000000.00000000000000000</WarlockTalents>
  <DruidTalents>0000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0000000000000000000000000</DruidTalents>
  <DeathKnightTalents>0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.000000000000000000000000000000000</DeathKnightTalents>
  <CustomItemInstances />
  <WaistBlacksmithingSocketEnabled>true</WaistBlacksmithingSocketEnabled>
  <HandsBlacksmithingSocketEnabled>false</HandsBlacksmithingSocketEnabled>
  <WristBlacksmithingSocketEnabled>false</WristBlacksmithingSocketEnabled>
  <PrimaryProfession>None</PrimaryProfession>
  <SecondaryProfession>None</SecondaryProfession>
</Character>"""
