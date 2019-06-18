CREATE TABLE IF NOT EXISTS CHANNEL(
    guildID     INTEGER PRIMARY KEY NOT NULL,
    townID      INTEGER DEFAULT NULL,
    dungeonID   INTEGER DEFAULT NULL,
    prefix      TEXT);

--entity-component system
CREATE TABLE IF NOT EXISTS ITEM_LIST(
    itemID      INTEGER PRIMARY KEY NOT NULL,
    name        TEXT UNIQUE NOT NULL,
    cost        INTEGER NOT NULL);
-- armor/weapon/skill/shop gold costs


CREATE TABLE IF NOT EXISTS ADVENTURER_LIST(
    advID           INTEGER PRIMARY KEY NOT NULL,
    class           TEXT NOT NULL UNIQUE,
    max_hp          INTEGER NOT NULL,
    dodge           INTEGER NOT NULL,
    prot            INTEGER NOT NULL,
    spd             INTEGER NOT NULL,
    acc             INTEGER NOT NULL,
    crit            INTEGER NOT NULL,
    dmg_lower       INTEGER NOT NULL,
    dmg_upper       INTEGER NOT NULL,
    stun_res        INTEGER NOT NULL,
    blight_res      INTEGER NOT NULL,
    disease_res     INTEGER NOT NULL,
    death_blow_res  INTEGER NOT NULL,
    move_res        INTEGER NOT NULL,
    bleed_res       INTEGER NOT NULL,
    debuff_res      INTEGER NOT NULL,
    trap_res        INTEGER NOT NULL);
-- crit bonus buff


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


CREATE TABLE IF NOT EXISTS MONSTER_LIST(
    monster         INTEGER PRIMARY KEY NOT NULL,
    name            TEXT NOT NULL UNIQUE,
    max_hp          INTEGER NOT NULL,
    dodge           INTEGER NOT NULL,
    prot            INTEGER NOT NULL,
    spd             INTEGER NOT NULL,
    acc             INTEGER NOT NULL,
    crit            INTEGER NOT NULL,
    dmg_lower       INTEGER NOT NULL,
    dmg_upper       INTEGER NOT NULL,
    stun_res        INTEGER NOT NULL,
    blight_res      INTEGER NOT NULL,
    disease_res     INTEGER NOT NULL,
    death_blow_res  INTEGER NOT NULL,
    move_res        INTEGER NOT NULL,
    bleed_res       INTEGER NOT NULL,
    debuff_res      INTEGER NOT NULL,
    trap_res        INTEGER NOT NULL);


CREATE TABLE IF NOT EXISTS EFFECT_LIST(effectID PRIMARY KEY NOT NULL);
-- needs completion


CREATE TABLE IF NOT EXISTS SKILL_LIST(skillID PRIMARY KEY NOT NULL);
-- needs completion


CREATE TABLE IF NOT EXISTS QUIRK_LIST(quirkID PRIMARY KEY NOT NULL);
-- needs completion




CREATE TABLE IF NOT EXISTS PLAYERS(
    playerID                    INTEGER PRIMARY KEY NOT NULL,
    gold                        INTEGER NOT NULL DEFAULT 0,
    busts                       INTEGER NOT NULL DEFAULT 0,
    portraits                   INTEGER NOT NULL DEFAULT 0,
    deeds                       INTEGER NOT NULL DEFAULT 0,
    crests                      INTEGER NOT NULL DEFAULT 0,
    blacksmith_weapon_level     INTEGER NOT NULL DEFAULT 0,
    blacksmith_armor_level      INTEGER NOT NULL DEFAULT 0,
    blacksmith_discount_level   INTEGER NOT NULL DEFAULT 0,
    guild_skill_level_cap       INTEGER NOT NULL DEFAULT 0,
    guild_discount_level        INTEGER NOT NULL DEFAULT 0,
    nomad_trinket_count         INTEGER NOT NULL DEFAULT 0,
    nomad_discount_level        INTEGER NOT NULL DEFAULT 0,
    sanitarium_discount_level   INTEGER NOT NULL DEFAULT 0,
    stagecoach_size             INTEGER NOT NULL DEFAULT 0,
    stagecoach_level_cap        INTEGER NOT NULL DEFAULT 0,
    roster_size_level           INTEGER NOT NULL DEFAULT 0,
    survivalist_discount_level  INTEGER NOT NULL DEFAULT 0);


CREATE TABLE IF NOT EXISTS TOWN_BASE_COST(
    name                TEXT PRIMARY KEY NOT NULL,
    busts               INTEGER NOT NULL,
    portraits           INTEGER NOT NULL,
    deeds               INTEGER NOT NULL,
    crests              INTEGER NOT NULL);

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


CREATE TABLE IF NOT EXISTS TOWN_UPGRADE_COST(
    name                TEXT PRIMARY KEY NOT NULL,
    busts               INTEGER NOT NULL,
    portraits           INTEGER NOT NULL,
    deeds               INTEGER NOT NULL,
    crests              INTEGER NOT NULL);

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


CREATE TABLE IF NOT EXISTS ADVENTURERS(
    heroID INTEGER PRIMARY KEY NOT NULL,
    advID INTEGER NOT NULL,
    playerID INTEGER NOT NULL,
    name TEXT NOT NULL,
    level INTEGER NOT NULL,
    hp INTEGER NOT NULL,
    stress INTEGER NOT NULL DEFAULT 0,
    exp INTEGER NOT NULL DEFAULT 0,
    weapon_level INTEGER NOT NULL DEFAULT 0,
    armor_level INTEGER NOT NULL DEFAULT 0,
    status TEXT NOT NULL DEFAULT 'ALIVE',
    FOREIGN KEY(advID) REFERENCES ADVENTURER_LIST(advID),
    FOREIGN KEY(playerID) REFERENCES PLAYERS(playerID));


CREATE TABLE IF NOT EXISTS STAGECOACH(
    stagecoachID INTEGER PRIMARY KEY NOT NULL,
    playerID INTEGER NOT NULL,
    advID INTEGER NOT NULL,
    name TEXT NOT NULL,
    level INTEGER NOT NULL,
    time INTEGER NOT NULL,
    FOREIGN KEY(advID) REFERENCES ADVENTURER_LIST(advID),
    FOREIGN KEY(playerID) REFERENCES PLAYERS(playerID));


CREATE TABLE IF NOT EXISTS PARTY(
    partyID                 INTEGER PRIMARY KEY NOT NULL,
    guildID                 INTEGER UNIQUE NOT NULL,
    leaderID                INTEGER NOT NULL,
    pos1                    INTEGER NOT NULL,
    pos2                    INTEGER NOT NULL,
    pos3                    INTEGER NOT NULL,
    pos4                    INTEGER NOT NULL,
    FOREIGN KEY(guildID)    REFERENCES CHANNEL(guildID),
    FOREIGN KEY(leaderID)   REFERENCES PLAYERS(playerID),
    FOREIGN KEY(pos1)       REFERENCES ADVENTURERS(advID),
    FOREIGN KEY(pos2)       REFERENCES ADVENTURERS(advID),
    FOREIGN KEY(pos3)       REFERENCES ADVENTURERS(advID),
    FOREIGN KEY(pos4)       REFERENCES ADVENTURERS(advID));


-- CREATE TABLE IF NOT EXISTS DUNGEON(dungeonID)
-- Needs completion


CREATE TABLE IF NOT EXISTS QUIRKS(
    quirkID INTEGER NOT NULL,
    heroID INTEGER NOT NULL,
    PRIMARY KEY(quirkID, heroID),
    FOREIGN KEY(quirkID) REFERENCES QUIRK_LIST(quirkID),
    FOREIGN KEY(heroID) REFERENCES ADVENTURERS(heroID));


CREATE TABLE IF NOT EXISTS INVENTORY(
    itemID INTEGER NOT NULL,
    playerID INTEGER NOT NULL,
    PRIMARY KEY(itemID, playerID),
    FOREIGN KEY(itemID) REFERENCES ITEM_LIST(itemID),
    FOREIGN KEY(playerID) REFERENCES PLAYERS(playerID));


CREATE TABLE IF NOT EXISTS TRINKETS(
    itemID INTEGER NOT NULL,
    heroID INTEGER NOT NULL,
    PRIMARY KEY(itemID, heroID),
    FOREIGN KEY(itemID) REFERENCES ITEM_LIST(itemID),
    FOREIGN KEY(heroID) REFERENCES ADVENTURERS(heroID));


CREATE TABLE IF NOT EXISTS SKILLS(
    skillID INTEGER NOT NULL,
    heroID INTEGER NOT NULL,
    PRIMARY KEY(skillID, heroID),
    FOREIGN KEY(skillID) REFERENCES SKILL_LIST(skillID),
    FOREIGN KEY(heroID) REFERENCES ADVENTURERS(heroID));


CREATE TABLE IF NOT EXISTS EFFECTS(
    effectID INTEGER NOT NULL,
    heroID INTEGER NOT NULL,
    PRIMARY KEY(effectID, heroID),
    FOREIGN KEY(effectID) REFERENCES EFFECT_LIST(effectID),
    FOREIGN KEY(heroID) REFERENCES ADVENTURERS(heroID));