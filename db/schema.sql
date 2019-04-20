CREATE TABLE IF NOT EXISTS CHANNEL(
    guildID     INTEGER PRIMARY KEY NOT NULL,
    townID      INTEGER,
    dungeonID   INTEGER,
    prefix      TEXT);


CREATE TABLE IF NOT EXISTS ITEM_LIST(
    itemID      INTEGER PRIMARY KEY NOT NULL,
    name        TEXT UNIQUE NOT NULL,
    cost        INTEGER NOT NULL);


CREATE TABLE IF NOT EXISTS ADVENTURER_LIST(
    advID           INTEGER PRIMARY KEY NOT NULL,
    name            TEXT NOT NULL UNIQUE,
    hp              INTEGER NOT NULL,
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
-- INSERT OR IGNORE INTO ADVENTURER LIST VALUES(1, "Abomination")
-- INSERT OR IGNORE INTO ADVENTURER LIST VALUES(2, "Antiquarian")
-- INSERT OR IGNORE INTO ADVENTURER LIST VALUES(3, "Arbalest")
-- INSERT OR IGNORE INTO ADVENTURER LIST VALUES(4, "Bounty Hunter")
-- INSERT OR IGNORE INTO ADVENTURER LIST VALUES(5, "Crusader")
-- INSERT OR IGNORE INTO ADVENTURER LIST VALUES(6, "Flagellant")
-- INSERT OR IGNORE INTO ADVENTURER LIST VALUES(7, "Grave Robber")
-- INSERT OR IGNORE INTO ADVENTURER LIST VALUES(8, "Hellion")
-- INSERT OR IGNORE INTO ADVENTURER LIST VALUES(9, "Highwayman")
-- INSERT OR IGNORE INTO ADVENTURER LIST VALUES(10, "Hound Master")
-- INSERT OR IGNORE INTO ADVENTURER LIST VALUES(11, "Jester")
-- INSERT OR IGNORE INTO ADVENTURER LIST VALUES(12, "Leper")
-- INSERT OR IGNORE INTO ADVENTURER LIST VALUES(13, "Man At Arms")
-- INSERT OR IGNORE INTO ADVENTURER LIST VALUES(14, "Occultist")
-- INSERT OR IGNORE INTO ADVENTURER LIST VALUES(15, "Plague Doctor")
-- INSERT OR IGNORE INTO ADVENTURER LIST VALUES(16, "Shieldbreaker")
-- INSERT OR IGNORE INTO ADVENTURER LIST VALUES(17, "Vestal")


-- CREATE TABLE IF NOT EXISTS MONSTER_LIST(monsterID) (monster stuff)


-- CREATE TABLE IF NOT EXISTS EFFECT_LIST(effectID PRIMARY EKY NOT NULL, effect_name) (afflictions and stress too?)


-- CREATE TABLE IF NOT EXISTS SKILL_LIST(skillID)


-- CREATE TABLE IF NOT EXISTS QUIRK_LIST(quirkID)




-- CREATE TABLE IF NOT EXISTS INVENTORY(itemID)


-- CREATE TABLE IF NOT EXISTS ADVENTURERS(status TEXT)


-- CREATE TABLE IF NOT EXISTS PLAYERS(playerID PRIMARY KEY NOT NULL, gold INTEGER NOT NULL) (Heirlooms)


-- CREATE TABLE IF NOT EXISTS SKILLS(skillID)


-- CREATE TABLE IF NOT EXISTS EFFECTS(effectID)


-- CREATE TABLE IF NOT EXISTS PARTY(partyID)


-- CREATE TABLE IF NOT EXISTS QUIRKS(quirkID, advID)