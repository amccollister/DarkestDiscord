-- ADVENTURER_LIST data insertion --

INSERT OR IGNORE INTO ADVENTURER_LIST VALUES(1, "Abomination", 26, 8, 0, 7, 0, 2, 6, 11, 40, 60, 20, 67, 40, 30, 20, 10);
INSERT OR IGNORE INTO ADVENTURER_LIST VALUES(2, "Antiquarian", 17, 10, 0, 5, 0, 1, 3, 5, 20, 20, 20, 67, 20, 20, 20, 10);
INSERT OR IGNORE INTO ADVENTURER_LIST VALUES(3, "Arbalest", 27, 0, 0, 3, 0, 6, 4, 8, 40, 30, 30, 67, 40, 30, 30, 10);
INSERT OR IGNORE INTO ADVENTURER_LIST VALUES(4, "Bounty Hunter", 25, 5, 0, 5, 0, 4, 5, 10, 40, 30, 20, 67, 40, 30, 30, 40);
INSERT OR IGNORE INTO ADVENTURER_LIST VALUES(5, "Crusader", 33, 5, 0, 1, 0, 3, 6, 12, 40, 30, 30, 67, 40, 30, 30, 10);
INSERT OR IGNORE INTO ADVENTURER_LIST VALUES(6, "Flagellant", 22, 0, 0, 6, 0, 2, 3, 6, 50, 30, 40, 73, 50, 65, 30, 0);
INSERT OR IGNORE INTO ADVENTURER_LIST VALUES(7, "Grave Robber", 20, 10, 0, 8, 0, 6, 4, 8, 20, 50, 30, 67, 20, 30, 30, 50);
INSERT OR IGNORE INTO ADVENTURER_LIST VALUES(8, "Hellion", 26, 10, 0, 4, 0, 5, 6, 12, 40, 40, 30, 67, 40, 40, 30, 20);
INSERT OR IGNORE INTO ADVENTURER_LIST VALUES(9, "Highwayman", 23, 10, 0, 5, 0, 5, 5, 10, 30, 30, 30, 67, 30, 30, 30, 40);
INSERT OR IGNORE INTO ADVENTURER_LIST VALUES(10, "Hound Master", 21, 10, 0, 5, 0, 4, 4, 7, 40, 40, 30, 67, 40, 40, 30, 40);
INSERT OR IGNORE INTO ADVENTURER_LIST VALUES(11, "Jester", 19, 15, 0, 7, 0, 4, 4, 7, 20, 40, 20, 67, 20, 30, 40, 30);
INSERT OR IGNORE INTO ADVENTURER_LIST VALUES(12, "Leper", 35, 0, 0, 2, 0, 1, 8, 16, 60, 40, 20, 67, 60, 10, 40, 10);
INSERT OR IGNORE INTO ADVENTURER_LIST VALUES(13, "Man-at-Arms", 31, 5, 0, 3, 0, 2, 5, 9, 40, 30, 30, 67, 40, 40, 30, 10);
INSERT OR IGNORE INTO ADVENTURER_LIST VALUES(14, "Occultist", 19, 10, 0, 6, 0, 6, 4, 7, 20, 30, 40, 67, 20, 40, 60, 10);
INSERT OR IGNORE INTO ADVENTURER_LIST VALUES(15, "Plague Doctor", 22, 0, 0, 7, 0, 2, 4, 7, 20, 60, 50, 67, 20, 20, 50, 20);
INSERT OR IGNORE INTO ADVENTURER_LIST VALUES(16, "Shieldbreaker", 20, 8, 0, 5, 0, 6, 5, 10, 50, 20, 30, 67, 50, 30, 30, 20);
INSERT OR IGNORE INTO ADVENTURER_LIST VALUES(17, "Vestal", 24, 0, 0, 4, 0, 1, 4, 8, 30, 30, 30, 67, 30, 40, 30, 10);
-------------------------------------------------------------------------------------------------------------------------------



-- TOWN_BASE_COST data insertion --

INSERT OR IGNORE INTO TOWN_BASE_COST VALUES("blacksmith_weapon_level", 0, 0, 8, 8);
INSERT OR IGNORE INTO TOWN_BASE_COST VALUES("blacksmith_armor_level", 0, 0, 8, 8);
INSERT OR IGNORE INTO TOWN_BASE_COST VALUES("blacksmith_discount_level", 0, 0, 4, 4);
INSERT OR IGNORE INTO TOWN_BASE_COST VALUES("guild_skill_level_cap", 0, 6, 0, 14);
INSERT OR IGNORE INTO TOWN_BASE_COST VALUES("guild_discount_level", 0, 2, 0, 6);
INSERT OR IGNORE INTO TOWN_BASE_COST VALUES("nomad_trinket_count", 0, 0, 0, 10);
INSERT OR IGNORE INTO TOWN_BASE_COST VALUES("nomad_discount_level", 0, 0, 0, 8);
INSERT OR IGNORE INTO TOWN_BASE_COST VALUES("sanitarium_discount_level", 5, 0, 0, 5);
INSERT OR IGNORE INTO TOWN_BASE_COST VALUES("stagecoach_size", 0, 0, 3, 4);
INSERT OR IGNORE INTO TOWN_BASE_COST VALUES("stagecoach_level_cap", 9, 0, 0, 12);
INSERT OR IGNORE INTO TOWN_BASE_COST VALUES("roster_size_level", 0, 0, 3, 4);
INSERT OR IGNORE INTO TOWN_BASE_COST VALUES("survivalist_discount_level", 0, 0, 0, 15);
----------------------------------------------------------------------------------------



-- TOWN_UPGRADE_COST data insertion --

INSERT OR IGNORE INTO TOWN_UPGRADE_COST VALUES("blacksmith_weapon_level", 0, 0, 12, 12);
INSERT OR IGNORE INTO TOWN_UPGRADE_COST VALUES("blacksmith_armor_level", 0, 0, 12, 12);
INSERT OR IGNORE INTO TOWN_UPGRADE_COST VALUES("blacksmith_discount_level", 0, 0, 5, 6);
INSERT OR IGNORE INTO TOWN_UPGRADE_COST VALUES("guild_skill_level_cap", 0, 10, 0, 15);
INSERT OR IGNORE INTO TOWN_UPGRADE_COST VALUES("guild_discount_level", 0, 3, 0, 10);
INSERT OR IGNORE INTO TOWN_UPGRADE_COST VALUES("nomad_trinket_count", 0, 0, 0, 16);
INSERT OR IGNORE INTO TOWN_UPGRADE_COST VALUES("nomad_discount_level", 0, 0, 0, 16);
INSERT OR IGNORE INTO TOWN_UPGRADE_COST VALUES("sanitarium_discount_level", 5, 0, 0, 5);
INSERT OR IGNORE INTO TOWN_UPGRADE_COST VALUES("stagecoach_size", 0, 0, 5, 6);
INSERT OR IGNORE INTO TOWN_UPGRADE_COST VALUES("stagecoach_level_cap", 3, 0, 0, 4);
INSERT OR IGNORE INTO TOWN_UPGRADE_COST VALUES("roster_size_level", 0, 0, 5, 6);
INSERT OR IGNORE INTO TOWN_UPGRADE_COST VALUES("survivalist_discount_level", 0, 0, 0, 20);
------------------------------------------------------------------------------------------



-- MONSTER_LIST data insertion --


------------------------------------------------------------------------------------------



-- ITEM_LIST data insertion --


------------------------------------------------------------------------------------------



-- QUIRK_LIST data insertion --


------------------------------------------------------------------------------------------



-- EFFECT_LIST data insertion --


------------------------------------------------------------------------------------------



-- TRINKET_LIST data insertion --


------------------------------------------------------------------------------------------



-- SKILL_LIST data insertion --


------------------------------------------------------------------------------------------



-- SKILL_EFFECT data insertion --


------------------------------------------------------------------------------------------