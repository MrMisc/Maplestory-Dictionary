
@client.command(brief = "<bossname = Name of boss you want to see information on> <attribute = feature of boss such as entry, pdr, ideal ied, ideal arc | by default set to None>", description = "Bossname is required but you do not need to ask for exact attribute. Typing nothing in attribute parameter section allows you to see all the information beautifully in one embed message. Please take note that any names you try have to have no spacing in them or else it won't work!")
async def boss(ctx, bossname, attribute = None):
    diction = {"Guard Captain Darknell[NormalMode] | nDarknell | Dunkell[NormalMode] | nDunkell":{"HP":"\n 26 trillion","PDR":"300%","Level":"265", "img":"https://cdn.discordapp.com/attachments/837052860700295208/970550487143284776/Mob_Guard_Captain_Darknell.webp",
    "Ideal IED & Ideal ARC":" Around 93-94% to deal 80% of your damage\n850 ARC to deal normal damage, 1,105~1,274 ARC to deal 30% more, 1275 to deal 50% more\n",
    "Entry":"• Require lv 255+. Recommend to be level 260+ due to level difference damage reduction (For Reboot:level 255 means 50% damage reduction)\n• One entry a day (separate from normal)\n• One clear a week (shared with normal)\n• Must have completed Esfera questline",
    "Guide":"...",
    "Notable Drops":"Up to 3 Captain Darknell's Soul Shard (individual drop, collect 10 to exchange for a random Captain Darknell Soul)"
                                         } ,

    "Will[HardMode] | hWill":{"HP":"\n• Phase 1: 42 trillion\n• Phase 2: 31.5 trillion\n• Phase 3: 52.5 trillion","PDR":"300%","Level":"250", "img":"https://cdn.discordapp.com/attachments/83566743976411136/970537953917042708/Hwill.gif",
    "Ideal IED & Ideal ARC":" Around 93-94% to deal 80% of your damage\n760 ARC to deal normal damage, 836-987 ARC to deal 30% more, 1140 to deal 50% more\n",
    "Entry":"• Require lv 235+. Recommend to be level 250+ due to level difference damage reduction (For Reboot:level 240 means 50% damage reduction)\n• One entry a day (separate from normal)\n• One clear a week (shared with normal)\n• Must have completed Esfera questline",
    "Guide":"https://forums.maplestory.nexon.net/discussion/22303/will-boss-guide \n https://www.youtube.com/watch?v=RrGGCkzid0o for an in-depth guide\n Probably recommend being about lvl 250 to fight this boss in Reboot since this guy is actually lvl 250 o3o",
    "Notable Drops":"• 2-3 Stone Cobweb Droplet (individual drop), 1 can be combined with 9 Stone Origin droplets (dropped from mobs in Esfera, Sellas and Tenebris Area) to get 1 Arachno coin, used to buy Arcane Umbra gears from NPC Dimo in Esfera Base Camp \n• [Instanced Drop] Up to 3 Will's Soul Shard \n• Arcane Umbra Armor Box, Arcane Umbra Weapon Box (untradeable, expires in 7 days, unaffected by drop rate increasing effects including Reboot world passive. Resulting item is tradable until equipped and does not expire)\n• Cursed Spellbook Box (low drop rate, untradeable, expires in 7 days. Resulting item is a Level 160 pocket item, 20 INT/STR/LUK/DEX respectively for Blue/Red/Green/Yellow, 10 for the other 3 stats each, 100 HP, 100 MP, 10 ATT, part of Pitched/Black Boss Accessory Set, tradable until equipped and does not expire) \n• [Instanced Drop] Mirror World Nodestone (provides 1 Level 1 Arachnid Reflection node)"
                                         } ,

"Will[NormalMode] | nWill":{"HP":"\n• Phase 1: 8.4 trillion\n• Phase 2: 6.3 trillion\n• Phase 3: 10.5 trillion","PDR":"300%","Level":"250", "img":"https://cdn.discordapp.com/attachments/837052860700295208/924321756779528242/will.gif",
    "Notable Drops":"• 1-2 Stone Cobweb Droplet (individual drop), 1 can be combined with 9 Stone Origin droplets (dropped from mobs in Esfera, Sellas and Tenebris Area) to get 1 Arachno coin, used to buy Arcane Umbra gears from NPC Dimo in Esfera Base Camp \n• [Instanced Drop] Up to 3 Will's Soul Shard ",
    "Ideal IED":" Around 93-94% to deal 80% of your damage\n",
    "Ideal ARC":" 760 ARC to deal normal damage, 836-987 ARC to deal 30% more, 1140 to deal 50% more\n",
    "Entry":"• Require lv 235+. Recommend to be level 250+ due to level difference damage reduction (For Reboot:level 240 means 50% damage reduction)\n• One entry a day (separate from hard)\n• One clear a week (shared with hard)\n• Must have completed Esfera questline",
    "Guide":"https://forums.maplestory.nexon.net/discussion/22303/will-boss-guide \n https://www.youtube.com/watch?v=RrGGCkzid0o for an in-depth guide\n Probably recommend being about lvl 250 to fight this boss in Reboot since this guy is actually lvl 250 o3o"} ,

    "nGloom | Gloom(NormalMode)":{"HP":"26 trillion","PDR":"300%","Level":"255",
    "Ideal ARC":"• 730 Arcane Force/Power (ARC) is needed to deal normal damage during the battle. \n • 10% more damage if your ARC is 803-948\n• 30% more damage if your ARC is at 949-1094\n• 50% more damage if your ARC is at 1095 or more","img":"https://cdn.discordapp.com/attachments/837052860700295208/924263883793911868/gloom.gif",
    "Notable Drops":"•Crimson/Rainbow/Black/Unextinguished/Never-extinguishing/Black Never-extinguishing Resurrection flame  \n •Spark of Determination (used to unlock black mage fight)",
    "Ideal IED":" Around 93-94% to deal 80% of your damage\n",
    "Entry":"• Require lv 245\n• One entry/attempt a day \n• One clear a week (NOT shared with chaos version)\n• Must have completed Moonbridge region questline",
    "Guide":"**Misc** \n  Note drops are unaffected by drop rate gear"}  ,

     "cGloom | Gloom(ChaosMode)":{"HP":"114.6 trillion","PDR":"300%","Level":"255",
    "Ideal ARC":"• 730 Arcane Force/Power (ARC) is needed to deal normal damage during the battle. \n • 10% more damage if your ARC is 803-948\n• 30% more damage if your ARC is at 949-1094\n• 50% more damage if your ARC is at 1095 or more","img":"https://cdn.discordapp.com/attachments/837052860700295208/924268502792151070/cgloom.gif",
    "Notable Drops":"•Crimson/Rainbow/Black/Unextinguished/Never-extinguishing/Black Never-extinguishing Resurrection flame\n •Spark of Determination (used to unlock black mage fight) \n •Endless Terror Ring, which is **part of the Pitched Boss Set**",
    "Ideal IED":" Around 93-94% to deal 80% of your damage\n",
    "Entry":"• Require lv 245\n• One entry/attempt a day \n• One clear a week (NOT shared with chaos version)\n• Must have completed Moonbridge region questline",
    "Guide":"**Misc** \n  Note drops are unaffected by drop rate gear"}  ,

     "nGuardianAngelSlime[NormalMode] | nGASlime":{"HP":"5 trillion","PDR":"300%","Level":"220", "img":"https://static.wikia.nocookie.net/maplestory/images/0/0f/Mob_Guardian_Angel_Slime.png/revision/latest/scale-to-width-down/476?cb=20210805090938",
    "Notable Drops":"• Guardian Angel Ring (low drop rate, Level 160 eye accessory, 5 all stats, 2 ATT/ 2 MATT, part of Boss Accessory Set)",
    "Ideal IED":" Around 93-94% to deal 80% of your damage\n",
    "Entry":"• Require lv 210+\n• One entry a day\n• One clear a week (shared with normal)\n• Must have completed [Ramuramu] Who's the Cutest of Them All ",
    "Guide":"https://docs.google.com/document/d/1O9jWeH68i5sUrOIYWO-OpdWPsTIyFgN0uspZ3xax0bA/edit \n You access [Ramuramu] Who's the cutest of them all quest in the quest lightbulb, as a lvl 210 quest \n https://www.youtube.com/watch?v=d4s1RClYlOs for an in-depth guide\n"},

    "cGuardianAngelSlime[ChaosMode] | cGASlime":{"HP":"**115.5** trillion","PDR":"300%","Level":"250", "img":"https://cdn.discordapp.com/attachments/837052860700295208/923752080529821747/guardian-angel-slime-1.gif",
    "Notable Drops":"• Guardian Angel Ring (relatively much higher drop rate, Level 160 eye accessory, 5 all stats, 2 ATT/ 2 MATT, part of Boss Accessory Set)",
    "Ideal IED":" Around 93-94% to deal 80% of your damage\n",
    "Entry":"• Require lv 210+\n• One entry a day\n• One clear a week (shared with normal)\n• Must have completed [Ramuramu] Who's the Cutest of Them All ",
    "Guide":"https://docs.google.com/document/d/1O9jWeH68i5sUrOIYWO-OpdWPsTIyFgN0uspZ3xax0bA/edit \n You access [Ramuramu] Who's the cutest of them all quest in the quest lightbulb, as a lvl 210 quest \n https://www.youtube.com/watch?v=d4s1RClYlOs for an in-depth guide\n Probably recommend being about lvl 250 to fight this boss in Reboot since this guy is actually lvl 250 o3o"}  ,

    "Gollux[HardMode] / Hardlux":{"PDR":"150%", "HP":"75b x2 \n 15b crystal",
    "Ideal IED":"About 75 IED to deal 62.5% of your damage \n 80 IED for 70%",
    "Notable Drops":" 15-19 Gollux Coins \n Reinforced Belt and Earrings",
    "img":"https://static.wikia.nocookie.net/maplestory/images/b/b8/Mob_Gollux_Head.png/revision/latest/scale-to-width-down/816?cb=20140425054234",
    "Guide":"https://dexless.com/guides/gollux-guide-updated.129/"},
    "Gollux[HellMode] / Hellux":{"PDR":"250%", "img":"https://cdn.discordapp.com/attachments/891562421221732363/902718544712716358/gol.png", "HP":"350b x2 \n 70b crystal",
    "Ideal IED":"About 90 IED to deal 75% of your damage \n 80 IED only allows for 50% damage!","Notable Drops":" 20-25 Gollux Coins \n Superior Belt and Earrings", "Guide":"https://dexless.com/guides/gollux-guide-updated.129/"},
    "Mori Ranmaru [Hard Mode]":{"HP":"10.5b","PDR":"55%", "img":"https://static.wikia.nocookie.net/maplestory/images/c/c2/Mob_Mori_Ranmaru.png/revision/latest/scale-to-width-down/251?cb=20121217061710",
    "Notable Drops":" Amaterasu Equips \n Take note that you will need to fight Mitsuhide to leverage the full effect of this \n set which isn't even endgame, but notably strong",
    "Ideal IED":"40 IED deals 67% of your damage"},
    "Lucid[EasyMode] | elucid":{"HP":"\n• Phase 1: 6 trillion\n• Phase 2: 6 trillion","PDR":"300%", "img":" https://static.wikia.nocookie.net/maplestory/images/4/4a/NPCArtwork_Lucid_%285%29.png/revision/latest/scale-to-width-down/250?cb=20180420035123",
    "Notable Drops":" Nothing noteworthy for easy mode, drop soul shard if you want your waifu's soul in your weapon",
    "Ideal IED":" Around 93-94% to deal 80% of your damage\nAim for that 80% as Lucid is a near endgame boss with hard mechanics",
    "Ideal ARC":"• 360 Arcane Force/Power (ARC) is needed to deal normal damage during the battle. \n • 10% more damage if your ARC is 396-467\n• 30% more damage if your ARC is at 468-539\n• 50% more damage if your ARC is at 540 or more",
    "Entry":"• Require lv 220+\n• One entry a day (separate from normal, hard)\n• One clear a week (shared with normal, hard)\n• Must have completed the Lachelein storyline",
    "Guide":"https://strategywiki.org/wiki/MapleStory/Lucid OR https://maplestory.fandom.com/wiki/Lucid/Monster for an in-depth guide\nhttps://www.digitaltq.com/maplestory-lucid-boss-guide for a more visual guide"}
, "Lucid[NormalMode] | nlucid":{"HP":"\n• Phase 1: 12 trillion\n• Phase 2: 12 trillion","PDR":"300%", "img":"https://static.wikia.nocookie.net/maplestory/images/a/a1/NPCArtwork_Lucid_%287%29.png/revision/latest/scale-to-width-down/250?cb=20180420035124",
    "Notable Drops":"1~2 Butterfly Droplet Stones (individual drop, 1 can be combined with 9 Arcane River Droplet Stones dropping rarely from Lachelein, Arcana, Morass mobs to get 1 Phantasma Coin, which can be used to buy Arcane Umbra gears from Dimo)",
    "Ideal IED":" Around 93-94% to deal 80% of your damage\nAim for that 80% as Lucid is a near endgame boss with hard mechanics",
    "Ideal ARC":"• 360 Arcane Force/Power (ARC) is needed to deal normal damage during the battle. \n • 10% more damage if your ARC is 396-467\n• 30% more damage if your ARC is at 468-539\n• 50% more damage if your ARC is at 540 or more",
    "Entry":"• Require lv 220+\n• One entry a day (separate from ez, hard)\n• One clear a week (shared with ez, hard)\n• Must have completed the Lachelein storyline",
    "Guide":"https://strategywiki.org/wiki/MapleStory/Lucid OR https://maplestory.fandom.com/wiki/Lucid/Monster for an in-depth guide\nhttps://www.digitaltq.com/maplestory-lucid-boss-guide for a more visual guide"}
,"Lucid[HardMode] |hlucid":{"HP":"• Phase 1: 50.8 trillion\n• Phase 2: 50.8 trillion\n• Phase 3: 12 Trillion","PDR":"300%", "img":" https://static.wikia.nocookie.net/maplestory/images/a/a3/NPCArtwork_Lucid_%286%29.png/revision/latest/scale-to-width-down/250?cb=20180420035123",
    "Notable Drops":"• 2~3 Butterfly Droplet Stones (individual drop, 1 can be combined with 9 Arcane River Droplet Stones dropping rarely from Lachelein, Arcana, Morass mobs to get 1 Phantasma Coin, which can be used to buy Arcane Umbra gears from Dimo)\n• Arcane Umbra Gloves, Shoes, Capes, Weapons (low chance, unaffected by drop rate increasing effects) \n • Dreamy Belt (low drop rate, Level 200 belt, 50 all stats, 6 ATT, 3 upgrade slots, part of Black Boss Accessory Set)",
    "Ideal IED":" Around 93-94% to deal 80% of your damage, 90% to deal 70% damage\nAim for that 80% as Lucid is a near endgame boss with hard mechanics",
    "Ideal ARC":"• 360 Arcane Force/Power (ARC) is needed to deal normal damage during the battle. \n • 10% more damage if your ARC is 396-467\n• 30% more damage if your ARC is at 468-539\n• 50% more damage if your ARC is at 540 or more",
    "Entry":"• Require lv 220+\n• One entry a day (separate from ez, normal)\n• One clear a week (shared with ez, normal)\n• Must have completed the Lachelein storyline",
    "Guide":"(Highly recommended to read about her phrase 3 for her hard mode special phase)\nhttps://strategywiki.org/wiki/MapleStory/Lucid OR https://maplestory.fandom.com/wiki/Lucid/Monster for an in-depth guide\nhttps://www.digitaltq.com/maplestory-lucid-boss-guide for a more visual guide"},
    "Damien[NormalMode] | ndamien":{"HP":"\n• Phase 1: 840 billion\n• Phase 2: 360 billion","PDR":"300%", "img":" https://cdn.discordapp.com/attachments/837052860700295208/905793275707936828/247.png",
    "Notable Drops":"• 1~3 Twisted Stigma Spirit Stones (individual drop, 1 can be combined with 20 Faint Stigma Spirit Stone, dropping rarely from Dark World Tree mobs or Dark World Tree weekly quest, to get 1 Stigma Coin, which can be used to buy Absolab gears from Supplier Salio)\n• Ruin Force Shield (low drop rate, Demon Aegis, Final Damage +10% but damage taken from enemy attacks +25% including %HP) ",
    "Ideal IED":" Around 93-94% to deal 80% of your damage\nAim for that 80% as Damien is a near endgame boss with complicated mechanics",
    "Entry":"• Require lv 190+\n• One entry a day\n• One clear a week (shared with hard)\n• Must have completed Heroes of Maple Act 4 "," ** ** " :" ** ** ** **",
    "Guide":"https://strategywiki.org/wiki/MapleStory/Damien OR https://maplestory.fandom.com/wiki/Damien/Monster for an in-depth guide\n https://www.digitaltq.com/maplestory-damien-boss-guide for a more visual guide"}
    ,"Zakum[EasyMode] | ezak":{"HP":"\n• Body: 2.2m\n• Arms(x8): 204,000","PDR":"\n• Body: 30%\n• Arms: 25%", "img":"https://static.wikia.nocookie.net/maplestory/images/4/43/Mob_Zakum.png/revision/latest/scale-to-width-down/350?cb=20201214015649",
    "Notable Drops":"\n• Zakum's Tree Branch\n• Zakum Helmet\n• Zakum's Soul Shard",
    "Ideal IED":"No ideal IED needed",
    "Entry":"• Require lvl 50+\n• One entry a day (Shared with Normal)"," ** ** " :" ** ** ** **",
    "Guide":"https://maplestory.fandom.com/wiki/Zakum"},
    "Damien[HardMode] | hdamien":{"HP":"\n• Phase 1: 25.2 trillion\n• Phase 2: 10.8 trillion","PDR":"300%", "img":"https://cdn.discordapp.com/attachments/837052860700295208/905831363838607380/185.png",
    "Ideal IED":" Around 93-94% to deal 80% of your damage\nAim for that 80% as Damien is a near endgame boss with complicated mechanics",
    "Entry":"• Require lv 190+\n• One entry a day\n• One clear a week (shared with normal)\n• Must have completed Heroes of Maple Act 4 ",
    "Item Drops":"• 2~4 Twisted Stigma Spirit Stones (individual drop, 1 can be combined with 20 Faint Stigma Spirit Stone, dropping rarely from Dark World Tree mobs or Dark World Tree weekly quest, to get 1 Stigma Coin, which can be used to buy Absolab gears from Supplier Salio)","Weapon Drop":"\n• Ruin Force Shield (low drop rate, Demon Aegis, Final Damage +10% but damage taken from enemy attacks +25% including %HP)\n• Absolabs Hat, Overall, Shoulder, Weapons (unaffected by drop rate increasing effects)\n•  Magic Eyepatch (low drop rate, Level 160 eye accessory, 15 all stats, 3 ATT, 3 upgrade slots, part of Black Boss Accessory Set)",
    "Guide":"https://strategywiki.org/wiki/MapleStory/Damien OR https://maplestory.fandom.com/wiki/Damien/Monster for an in-depth guide\n https://www.digitaltq.com/maplestory-damien-boss-guide for a more visual guide"},
    "Zakum[NormalMode] | nzak":{"HP":"\n• Body: 7m\n• Arms(x8): 700,000","PDR":"\n• Body: 40%\n• Arms: 40%", "img":"https://static.wikia.nocookie.net/maplestory/images/b/b2/Soul_Collector_Artwork_Zakum_%281%29.png/revision/latest/scale-to-width-down/171?cb=20180811122254",
    "Notable Drops":"\n• Zakum's Tree Branch\n• Zakum Helmet\n• Zakum's Soul Shard\n• Aquatic Letter Eye Accessories\n• Condensed Power Crystal",
    "Ideal IED":"No ideal IED needed",
    "Entry":"• Require lvl 90+\n• One entry a day (Shared with Easy)"," ** ** ":"** ** ** **",
    "Guide":"https://maplestory.fandom.com/wiki/Zakum"},
    "Lotus[NormalMode] | nlotus":{"HP":"\n• Phase 1: 400 billion\n• Phase 2: 400 billion\n• Phase 3: 710 billion","PDR":"300%", "img":"https://static.wikia.nocookie.net/maplestory/images/5/58/Soul_Collector_Artwork_Lotus_%282%29.png/revision/latest/scale-to-width-down/247?cb=20180113230240",
    "Notable Drops":"1~3 S-Grade Energy Hypercore (individual drop, 1 can be combined with 20 Diffusion-Line Energy Core (Grade A), dropping rarely from Scrapyard mobs or Scrapyard weekly quest, to get 1 AbsoLab Coin, which can be used to buy Absolab gears from Three-Hands)",
    "Ideal IED":" Around 93-94% to deal 80% of your damage\nAim for that 80% as Lotus is a near endgame boss with complicated mechanics",
    "Entry":"• Require lv 190+\n• One entry a day\n• One clear a week (shared with hard)\n• Must have completed Black Haven "," ** ** " :" ** ** ** **",
    "Guide":" https://strategywiki.org/wiki/MapleStory/Lotus OR https://maplestory.fandom.com/wiki/Lotus/Monster for an in-depth guide\ https://www.digitaltq.com/maplestory-lotus-boss-guide for a more visual guide"},
    "AkechiMitsuhide":{"HP":"\n• Phase 1: 152b\n• Phase 2: 152b","PDR":"300%", "img":"https://cdn.discordapp.com/attachments/891562421221732363/906101573338423357/exp.fw.png",
    "Ideal IED":"90% IED to deal 70% of your damage",
    "Entry":"• Require lvl 200+\n• One entry a day\n• One clear a week","Equip Set Effect**":"• 5 set effect : +25 attk/mattk +10 %ied\n• 6 set effect: +45 attk/mattk +10%ied\n• 7 set effect: +75 attk/mattk +19\%ied\n• 8 set effect: +115 attk/mattk +19%ied + 30%BD\n• 9 set effect: +155 attk/mattk +27.1%ied + 30%BD +5% crit damage",
    "Notable Drops":"\n• Silver Wolf Weapon (Acts as a 2 piece set effect with HardRanmaru gears for a 9 set effect)\n• Note that the set name is different for each category of classes",
    "Guide":"https://maplestory.fandom.com/wiki/Akechi_Mitsuhide/Monster \n https://maplestory.fandom.com/wiki/Equipment_Set/Ame-no-Uzume_Set#Post_Sengoku_War"} ,
    "Lotus[HardMode] | hlotus":{"HP":"\n• Phase 1: 1.7 trillion\n• Phase 2: 7 trillion\n• Phase 3: 24.5 trillion","PDR":"300%", "img":"https://static.wikia.nocookie.net/maplestory/images/1/18/Artwork_Lotus_%28Black_Heaven%29.png/revision/latest/scale-to-width-down/885?cb=20141124153745",
    "Ideal IED":" Around 93-94% to deal 80% of your damage\nAim for that 80% as Lotus is a near endgame boss with complicated mechanics",
    "Entry":"• Require lv 190+\n• One entry a day\n• One clear a week (shared with normal)\n• Must have completed Black Haven",
    "Item Drops":"• 2~4 S-Grade Energy Hypercore (individual drop, 1 can be combined with 20 Diffusion-Line Energy Core (Grade A), dropping rarely from Scrapyard mobs or Scrapyard weekly quest, to get 1 AbsoLab Coin, which can be used to buy Absolab gears from Three-Hands)","Weapon Drop":"\n• Absolabs Glove, Shoes, Cape, Weapons (unaffected by drop rate increasing effects\n• Rogue Control Machine Mark (low drop rate, Level 160 face accessory, 10 all stats, 10 ATT, 5 upgrade slots, part of Black Boss Accessory Set)\n•  Damaged Black Heart (low drop rate, talk to Sensitive Squaroid in Scrapyard to exchange for Black Heart 20 days unextendable, with fixed potentials of +30% damage to boss monsters and +30% ignore DEF)",
    "Guide":" https://strategywiki.org/wiki/MapleStory/Lotus OR https://maplestory.fandom.com/wiki/Lotus/Monster for an in-depth guide\ https://www.digitaltq.com/maplestory-lotus-boss-guide for a more visual guide"},
    "PrincessNo | Pno":{"HP":"\n• 200b","PDR":"\n• 100%", "img":"https://cdn.discordapp.com/attachments/891562421221732363/906112586137882624/pno.png",
    "Ideal IED":"70% IED to deal 70% of your damage",
    "Entry":"• Require lvl 140+\n• One entry a day\n• One clear a week"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **",
    "Notable Drops":"\n• Kanna's Treasure\n• Hayato's Treasure\n• Ayame's Treasure\n• Princess No's Chair\n• Captivating Fragment (Exchange 15 for lvl 140 Secondary weapon"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **",
    "Guide":"https://maplestory.fandom.com/wiki/Princess_No"},
    "ChaosPapulatus | cPap":{"HP":"\n• Phase 0: 539,925 \n• Phase 1: 378b\n• Phase 2: 126b","PDR":"250%", "img":"https://cdn.discordapp.com/attachments/891562421221732363/906095628541657128/cpap.png",
    "Ideal IED":"92% IED to deal 80% of your damage at least",
    "Entry":"• Require lvl 190+\n• One entry every 30min\n• One clear a week",
    "Notable Drops":"Papulatus Mark (for transposing)"," ** ** " :" ** ** ** **",
    "Guide":"https://maplestory.fandom.com/wiki/Papulatus "},
    "nPierre[NormalMode]":{"HP":"\n• 315m","PDR":"\n• 50%", "img":"https://partycity6.scene7.com/is/image/PartyCity/_pdp_sq_?$_500x500_$&$product=PartyCity/176114",
    "Ideal IED":"50% IED to deal 75% of your damage",
    "Entry":"• Require lvl 125+\n• One entry every 30mins\n• One clear a day"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **",
    "Notable Drops":"\n• Pierre's hat\n• Happy Pierre's Chair"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **",
    "Guide":"https://maplestory.fandom.com/wiki/Pierre/Monster#Non-KMS"},
    "cPierre[ChaosMode]":{"HP":"\n• 80b","PDR":"\n• 80%", "img":"https://compote.slate.com/images/26572c3a-0e51-4a9f-9049-b64e730ca75d.jpg",
    "Ideal IED":"70% IED to deal 76% of your damage",
    "Entry":"• Require lvl 180+\n• One entry every 30mins\n• One clear a week",
    "Notable Drops":"\n• Pierre's hat\n• Happy Pierre's Chair\n• Piece of Mockery (Combine 5 to obtain a CRA Bottom)"
    , "Tips":"\n• If you are going for a bind, do not bind him when he is purple, he becomes bind immune and escapes \n• He splits at about 30%hp which is right around when the hp bar meets the death counter box" ,"Guide":"https://maplestory.fandom.com/wiki/Pierre/Monster#Non-KMS"},
    "cvonbon[ChaosMode]":{"HP":"\n• 100b","PDR":"\n• 100%", "img":"https://static.wikia.nocookie.net/chickenlittle/images/f/f2/Buck_Cluck_Thumbs_Up.jpg/revision/latest/scale-to-width-down/250?cb=20170317222342",
    "Ideal IED":"70% IED to deal 70% of your damage",
    "Entry":"• Require lvl 180+\n• One entry every 30mins\n• One clear a week"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **",
    "Notable Drops":"\n• Von Bon's Helmet\n• Von Bon's Von Chair\n• Piece of Time (Combine 5 to obtain a Top)"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **",
    "Guide":"https://maplestory.fandom.com/wiki/Von_Bon/Monster"},
    "cqueen":{"HP":"\n• 140b","PDR":"\n• 120%", "img":"https://ichef.bbci.co.uk/news/976/cpsprodpb/8EF6/production/_121189563_hi071452015.jpg",
    "Ideal IED":"80% IED to deal 76% of your damage",
    "Entry":"• Require lvl 180+\n• One entry every 30mins\n• One clear a week"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **",
    "Notable Drops":"\n• Queen's Tiara\n• Crimson Queen's Throne\n• Piece of Anguish (Combine 5 to obtain a Hat)"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **",
    "Guide":"https://maplestory.fandom.com/wiki/Crimson_Queen/Monster"} ,
    "cvell":{"HP":"\n• 200b","PDR":"\n• 200%", "img":"https://static.wikia.nocookie.net/maplestory/images/d/da/Mob_Vellum.png/revision/latest/scale-to-width-down/350?cb=20130110185030",
    "Ideal IED":"85% IED to deal 70% of your damage",
    "Entry":"• Require lvl 180+\n• One entry every 30mins\n• One clear a week"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **",
    "Notable Drops":"\n• Vellum's Helm\n• Vellum's Rock Chair\n• Piece of Destruction (Combine 15 to obtain a CRA Weapon)"," ** ** " :" ** ** ** **"," ** ** " :" ** ** ** **",
    "Guide":"https://maplestory.fandom.com/wiki/Vellum/Monster"}

}
    colours = np.random.randint(0, 0xffffff)
    # for key,value in diction.items():print(value)
    if attribute==None:
        keyname = list({key:value for key, value in diction.items() if key.lower().__contains__(bossname.lower())})
        KEYS = list({KEY:value[KEY] for key, value in diction.items() for KEY in value  if key.lower().__contains__(bossname.lower())})
        VALUES = [{KEY:value[KEY] for key, value in diction.items() for KEY in value if key.lower().__contains__(bossname.lower())}[item] for item in list({KEY:value[KEY] for key, value in diction.items() for KEY in value if key.lower().__contains__(bossname.lower())})]
        emb = discord.Embed(title = f"Stats for {keyname[0]}", color = colours)
        for i in range(len(KEYS)):
            if KEYS[i]!="img":
                emb.add_field(name = f'**{KEYS[i]}**', value = f'{VALUES[i]}' )
                emb.set_author(name = f"{ctx.author}", icon_url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.dribbble.com%2Fusers%2F2321305%2Fscreenshots%2F5389964%2Fmaplestory-01.png&f=1&nofb=1")
            else:
                try:
                    emb.set_image(url = f'{VALUES[i]}')
                except:
                    pass
        await ctx.send(content = None, embed = emb)
    else:
        KEYS = list({KEY:value[KEY] for key, value in diction.items() for KEY in value if key.lower().__contains__(bossname.lower()) if KEY.lower().__contains__(attribute.lower())})
        VALUES = [{KEY:value[KEY] for key, value in diction.items() for KEY in value if key.lower().__contains__(bossname.lower()) if KEY.lower().__contains__(attribute.lower())}[item] for item in list({KEY:value[KEY] for key, value in diction.items() for KEY in value if key.lower().__contains__(bossname.lower()) if KEY.lower().__contains__(attribute.lower())})]
        if (len(KEYS) == 1) and (len(VALUES) == 1):
            await ctx.send(f" `` {bossname} for {KEYS[0]} appears to return {VALUES[0]}, {ctx.author}. I hope I was of help '-'  ``")
