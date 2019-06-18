CREATE TABLE `DUNGEON`
(
  `guildID` INTEGER PRIMARY KEY,
  `town_channel` INTEGER,
  `dungeon_channel` INTEGER,
  `partyID` INTEGER,
  `dungeon_type` TEXT,
  `mission` TEXT,
   FOREIGN KEY (`partyID`) REFERENCES `PARTY` (`partyID`)
);

CREATE TABLE `ITEM_LIST`
(
  `itemID` INTEGER PRIMARY KEY,
  `name` TEXT UNIQUE NOT NULL,
  `cost` INTEGER NOT NULL,
  `stack_size` INTEGER NOT NULL,
  `type` TEXT NOT NULL
);

CREATE TABLE `TRINKET_LIST`
(
  `trinketID` INTEGER PRIMARY KEY,
  `itemID` INTEGER NOT NULL,
  `trinketName` TEXT,
   FOREIGN KEY (`itemID`) REFERENCES `ITEM_LIST` (`itemID`)
);

CREATE TABLE `TRINKET_EFFECT`
(
  `trinketID` INTEGER,
  `stat` TEXT NOT NULL,
  `modifier` INTEGER NOT NULL,
   FOREIGN KEY (`trinketID`) REFERENCES `TRINKET_LIST` (`trinketID`)
);

CREATE TABLE `ADVENTURER_LIST`
(
  `advID` INTEGER PRIMARY KEY,
  `class` TEXT UNIQUE NOT NULL,
  `max_hp` INTEGER NOT NULL,
  `dodge` INTEGER NOT NULL,
  `prot` INTEGER NOT NULL,
  `spd` INTEGER NOT NULL,
  `acc` INTEGER NOT NULL,
  `crit` INTEGER NOT NULL,
  `dmg_lower` INTEGER NOT NULL,
  `dmg_upper` INTEGER NOT NULL,
  `stun_res` INTEGER NOT NULL,
  `blight_res` INTEGER NOT NULL,
  `disease_res` INTEGER NOT NULL,
  `death_blow_res` INTEGER NOT NULL,
  `move_res` INTEGER NOT NULL,
  `bleed_res` INTEGER NOT NULL,
  `debuff_res` INTEGER NOT NULL,
  `trap_res` INTEGER NOT NULL,
  `stress_res` INTEGER NOT NULL,
  `virtue_chance` INTEGER NOT NULL,
  `crit_bonus` TEXT NOT NULL
);

CREATE TABLE `MONSTER_LIST`
(
  `monsterID` INTEGER PRIMARY KEY,
  `name` TEXT UNIQUE NOT NULL,
  `max_hp` INTEGER NOT NULL,
  `dodge` INTEGER NOT NULL,
  `prot` INTEGER NOT NULL,
  `spd` INTEGER NOT NULL,
  `acc` INTEGER NOT NULL,
  `crit` INTEGER NOT NULL,
  `dmg_lower` INTEGER NOT NULL,
  `dmg_upper` INTEGER NOT NULL,
  `stun_res` INTEGER NOT NULL,
  `blight_res` INTEGER NOT NULL,
  `disease_res` INTEGER NOT NULL,
  `death_blow_res` INTEGER NOT NULL,
  `move_res` INTEGER NOT NULL,
  `bleed_res` INTEGER NOT NULL,
  `debuff_res` INTEGER NOT NULL,
  `trap_res` INTEGER NOT NULL
);

CREATE TABLE `EFFECT_LIST`
(
  `effectID` INTEGER PRIMARY KEY,
  `name` TEXT,
  `stat` TEXT
);

CREATE TABLE `SKILL_LIST`
(
  `skillID` INTEGER PRIMARY KEY,
  `range` TEXT,
  `rank` INTEGER,
  `target` INTEGER,
  `target_ally` BOOLEAN,
  `damage_mod` INTEGER,
  `accuracy_mod` INTEGER,
  `crit_mod` INTEGER
);

CREATE TABLE `SKILL_EFFECT`
(
  `skillID` INTEGER,
  `stat` TEXT,
  `modifier` INTEGER,
  `self` BOOLEAN,
   FOREIGN KEY (`skillID`) REFERENCES `SKILL_LIST` (`skillID`)
);

CREATE TABLE `QUIRK_LIST`
(
  `quirkID` INTEGER PRIMARY KEY,
  `name` TEXT,
  `stat` TEXT
);

CREATE TABLE `PLAYERS`
(
  `playerID` INTEGER PRIMARY KEY,
  `gold` INTEGER NOT NULL,
  `busts` INTEGER NOT NULL,
  `portraits` INTEGER NOT NULL,
  `deeds` INTEGER NOT NULL,
  `crests` INTEGER NOT NULL,
  `blacksmith_weapon_level` INTEGER NOT NULL,
  `blacksmith_armor_level` INTEGER NOT NULL,
  `blacksmith_discount_level` INTEGER NOT NULL,
  `guild_skill_level_cap` INTEGER NOT NULL,
  `guild_discount_level` INTEGER NOT NULL,
  `nomad_trinket_count` INTEGER NOT NULL,
  `nomad_discount_level` INTEGER NOT NULL,
  `sanitarium_discount_level` INTEGER NOT NULL,
  `stagecoach_size` INTEGER NOT NULL,
  `stagecoach_level_cap` INTEGER NOT NULL,
  `roster_size_level` INTEGER NOT NULL,
  `survivalist_discount_level` INTEGER NOT NULL
);

CREATE TABLE `TOWN_BASE_COST`
(
  `name` TEXT PRIMARY KEY,
  `busts` INTEGER NOT NULL,
  `portraits` INTEGER NOT NULL,
  `deeds` INTEGER NOT NULL,
  `crests` INTEGER NOT NULL
);

CREATE TABLE `TOWN_UPGRADE_COST`
(
  `name` TEXT PRIMARY KEY,
  `busts` INTEGER NOT NULL,
  `portraits` INTEGER NOT NULL,
  `deeds` INTEGER NOT NULL,
  `crests` INTEGER NOT NULL
);

CREATE TABLE `ADVENTURERS`
(
  `heroID` INTEGER PRIMARY KEY,
  `advID` INTEGER NOT NULL,
  `playerID` INTEGER NOT NULL,
  `name` TEXT NOT NULL,
  `level` INTEGER NOT NULL,
  `hp` INTEGER NOT NULL,
  `stress` INTEGER NOT NULL,
  `exp` INTEGER NOT NULL,
  `weapon_level` INTEGER NOT NULL,
  `armor_level` INTEGER NOT NULL,
  `status` TEXT NOT NULL DEFAULT 'ALIVE'
);

CREATE TABLE `STAGECOACH`
(
  `stagecoachID` INTEGER PRIMARY KEY,
  `playerID` INTEGER NOT NULL,
  `advID` INTEGER NOT NULL,
  `name` TEXT NOT NULL,
  `level` INTEGER NOT NULL,
  `time` INTEGER NOT NULL,
  FOREIGN KEY (`advID`) REFERENCES `ADVENTURER_LIST` (`advID`),
  FOREIGN KEY (`playerID`) REFERENCES `PLAYERS` (`playerID`)
);

CREATE TABLE `PARTY`
(
  `partyID` INTEGER PRIMARY KEY,
  `leaderID` INTEGER NOT NULL,
  `pos1` INTEGER NOT NULL,
  `pos2` INTEGER NOT NULL,
  `pos3` INTEGER NOT NULL,
  `pos4` INTEGER NOT NULL,
  FOREIGN KEY (`leaderID`) REFERENCES `PLAYERS` (`playerID`),
  FOREIGN KEY (`pos1`) REFERENCES `ADVENTURERS` (`heroID`),
  FOREIGN KEY (`pos2`) REFERENCES `ADVENTURERS` (`heroID`),
  FOREIGN KEY (`pos3`) REFERENCES `ADVENTURERS` (`heroID`),
  FOREIGN KEY (`pos4`) REFERENCES `ADVENTURERS` (`heroID`)
);

CREATE TABLE `ROOM`
(
  `roomID` INTEGER PRIMARY KEY,
  `guildID` INTEGER,
  `room` BOOLEAN,
  `type` TEXT,
   FOREIGN KEY (`guildID`) REFERENCES `DUNGEON` (`guildID`)
);

CREATE TABLE `ROOM_ENEMY`
(
  `roomID` INTEGER,
  `monsterID` INTEGER,
  FOREIGN KEY (`roomID`) REFERENCES `ROOM` (`roomID`),
  FOREIGN KEY (`monsterID`) REFERENCES `MONSTER_LIST` (`monsterID`)
);

CREATE TABLE `ROOM_TREASURE`
(
  `roomID` INTEGER,
  `itemID` INTEGER,
  FOREIGN KEY (`roomID`) REFERENCES `ROOM` (`roomID`),
  FOREIGN KEY (`itemID`) REFERENCES `ITEM_LIST` (`itemID`)
);

CREATE TABLE `QUIRKS`
(
  `quirkID` INTEGER NOT NULL,
  `heroID` INTEGER NOT NULL,
  `modifier` INTEGER,
  FOREIGN KEY (`quirkID`) REFERENCES `QUIRK_LIST` (`quirkID`),
  FOREIGN KEY (`heroID`) REFERENCES `ADVENTURERS` (`heroID`)
);

CREATE TABLE `INVENTORY`
(
  `itemID` INTEGER NOT NULL,
  `playerID` INTEGER NOT NULL,
  FOREIGN KEY (`playerID`) REFERENCES `PLAYERS` (`playerID`),
  FOREIGN KEY (`itemID`) REFERENCES `ITEM_LIST` (`itemID`)
);

CREATE TABLE `TRINKETS`
(
  `heroID` INTEGER NOT NULL,
  `slot1` INTEGER,
  `slot2` INTEGER,
  FOREIGN KEY (`heroID`) REFERENCES `ADVENTURERS` (`heroID`),
  FOREIGN KEY (`slot1`) REFERENCES `TRINKET_LIST` (`trinketID`),
  FOREIGN KEY (`slot2`) REFERENCES `TRINKET_LIST` (`trinketID`)
);

CREATE TABLE `SKILLS`
(
  `skillID` INTEGER NOT NULL,
  `heroID` INTEGER NOT NULL,
  FOREIGN KEY (`skillID`) REFERENCES `SKILL_LIST` (`skillID`),
  FOREIGN KEY (`heroID`) REFERENCES `ADVENTURERS` (`heroID`)
);

CREATE TABLE `EFFECTS`
(
  `effectID` INTEGER NOT NULL,
  `heroID` INTEGER NOT NULL,
  `stat` TEXT,
  `modifier` INTEGER,
  `duration` INTEGER,
  FOREIGN KEY (`effectID`) REFERENCES `EFFECT_LIST` (`effectID`),
  FOREIGN KEY (`heroID`) REFERENCES `ADVENTURERS` (`heroID`)
);