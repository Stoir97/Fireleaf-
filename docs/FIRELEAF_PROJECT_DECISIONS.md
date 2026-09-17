# Fireleaf Project Decisions

This file records approved project-level decisions for the Fireleaf hack.

## Foundation

- Base: Pokemon Heart and Soul 2.0 (`pokehns-expansion`).
- Kanto target: Pokemon FireRed map, event, story, and progression fidelity.
- Kanto dialogue target: verbatim English Pokemon FireRed dialogue.
- Sevii Islands: excluded and ultimately replaced by Johto progression.
- Species scope: Kanto and Johto species form the regional base, with approved later evolutions.
- Pokedex structure: custom consecutive regional numbering, placing later evolutions alongside their evolutionary families rather than exposing gaps in National Dex numbering.
- Existing Heart and Soul 2.0 behavior remains the default unless explicitly changed here.

## Approved gameplay defaults

- Fairy type: enabled.
- Physical/Special split: modern, per-move categories.
- TMs: reusable.
- Base Shiny odds: 1/4096.
- Clock: hardware real-time clock.
- Shiny palettes: official/vanilla palettes, not alternate Modern Emerald palettes.
- No species or encounter is Shiny-locked. This applies globally to starters, gifts, fossils, static encounters, Legendary Pokemon, Mythical Pokemon, Celebi, and Mew.
- Static Legendary and Mythical Pokemon that are defeated respawn after Red enters the Hall of Fame again, unless an encounter has a separately documented special retry rule. Successfully catching the Pokemon permanently clears that encounter.
- Moltres is relocated from Sevii's Mt. Ember to a new volcanic area connected to Cinnabar Island.
- The Cinnabar volcanic area opens after Red earns the Volcano Badge from Blaine.
- FireRed's post-Blaine Bill event and the associated trip to One Island are removed completely. No replacement cutscene plays when Red exits the Gym; all unrelated Bill dialogue remains verbatim FireRed text.
- Before Blaine is defeated, a new guard NPC blocks the volcanic-area entrance and explains that only a Trainer who has defeated Blaine has demonstrated enough courage to enter. The NPC moves aside after the badge is obtained.
- After recognizing the Volcano Badge, the guard gives Red HM06 Rock Smash before moving aside. Rock Smash is used in the volcano's environmental puzzles and follows Heart and Soul's compatible-party-Pokemon field-move system.
- A new route extends west from Cinnabar Island and is explorable as soon as Cinnabar is reached.
- The new western route is named `Volcano Path` in the English location popup and Kanto region map.
- The new western route contains no Trainer battles and reuses Route 20's wild encounter table exactly, avoiding additional encounter-table complexity.
- The volcano entrance is located at the end of this route; only the volcano itself is badge-gated.
- Moltres is encountered at level 50, matching FireRed.
- The Cinnabar volcano is a completely new, extended multi-floor dungeon rather than a relocated Mt. Ember layout.
- The volcano has five principal sections: entrance, lower tunnels, magma chamber, upper tunnels, and Moltres crater.
- Its exploration layout is an interconnected labyrinth with cross-floor drops, loops, breakable rocks, movable boulders, optional item branches, and multiple routes that reconnect.
- Reaching the Moltres crater allows Red to open a permanent shortcut back to the volcano entrance, available on all later visits regardless of whether Moltres has been caught.
- Volcano Path and the Cinnabar volcano contain no Trainer battles. The dungeon challenge comes from exploration, wild encounters, and environmental puzzles, with Moltres as its primary static encounter.
- The volcano uses custom Kanto-only volcanic encounter tables rather than Mt. Ember or Pokemon Mansion tables. Candidate families include Geodude, Onix, Ponyta, Growlithe, Vulpix, and Magmar, with evolved forms distributed by depth.
- Following Pokemon: retained from Heart and Soul 2.0 throughout both Kanto and Johto. Map transitions, doors, stairs, Surf, bicycles, warps, and scripted scenes must be regression-tested with an active follower.
- Level-up learnsets: Generation 7 with Heart and Soul-specific adjustments.
- Field moves/HMs: retain the Heart and Soul 2.0 system; a compatible party Pokemon may perform the field move without occupying a move slot, subject to normal progression requirements.

## Heart and Soul systems policy

- Retain all systems already present in Heart and Soul 2.0.
- Use the Heart and Soul 2.0 `Recommended` preset as the default wherever the project already defines a recommended value.
- Preserve Heart and Soul's player-facing customization options unless they conflict with the 1-251 species limit, FireRed Kanto fidelity, removal of the Sevii Islands, or technical stability.
- Do not request individual approval for unchanged Heart and Soul defaults. Request a decision only for new features, unavoidable conflicts, or deviations from that base.

## Regional distribution and progression

- Kanto wild encounters use Kanto species only. Johto species must not appear as wild encounters in Kanto.
- Kanto encounter tables use FireRed as their base but also include LeafGreen-exclusive Kanto species, making all Kanto species obtainable without trading.
- LeafGreen-exclusive species are paired with their corresponding FireRed-exclusive species at comparable encounter rates rather than being restricted to rare slots.
- Kanto encounter tables do not vary by time of day. Day/night lighting remains active, but species and encounter rates stay constant.
- Modern party-wide Exp. Share is enabled from the beginning of Kanto.
- Exp. Share can be switched ON/OFF directly from the Options menu. This intentionally replaces Heart and Soul's existing Key Item toggle with a player option available from the start.
- Johto wild encounters predominantly use Johto species, with a minority of Kanto species.
- Ordinary Johto encounter tables target an average 70% Johto-species / 30% Kanto-species distribution, adjusted by each area's ecology rather than enforced identically on every map.
- Later-generation evolutions of Kanto and Johto species are included.
- Later-generation evolutions do not appear in wild encounter tables; they are obtained only by evolving their Kanto or Johto family members. Regional forms in the Johto Safari Zone remain the documented exception.
- Later-introduced baby Pokemon belonging to Kanto/Johto families are included: Azurill, Wynaut, Bonsly, Mime Jr., Happiny, Munchlax, and Mantyke.
- These baby Pokemon are obtainable only from Eggs, never through wild encounters, gifts, or the Safari Zone. Heart and Soul's modern breeding behavior applies, so Incense is not required.
- Kanto's Route 5 Day Care retains its original one-Pokemon FireRed behavior. Breeding and Egg production become available only at Johto's Day Care south of Goldenrod City, making later baby Pokemon post-League content.
- Link Cables are sold at the Celadon Department Store and replace mandatory multiplayer trades.
- Link Cables use Heart and Soul's existing 8,000 Pokeyen price, are consumable, and may be purchased repeatedly.
- Celadon begins selling Link Cables only after Red owns at least six Kanto badges.
- Mega Evolution remains disabled, matching Heart and Soul 2.0 defaults. Dynamax and Terastallization are likewise not introduced.

## S.S. Aqua and counterpart rival

- The first S.S. Aqua journey is explorable but has no missing-child quest.
- The ship reaches Olivine when the player enters the Captain's cabin.
- The unchosen player character waits in the cabin: Leaf if the player chose Red, or Red if the player chose Leaf.
- The counterpart introduces themself as the Captain's daughter/son and says they are traveling to Johto to collect the Johto badges and win the Pokemon League.
- The counterpart becomes a recurring rival during the Johto journey.
- When the Kanto League reopens after eight Johto badges, the counterpart replaces Blue as Champion.
- If the counterpart is Leaf, her Champion roster uses Let's Go Green's species: Clefable, Gengar, Kangaskhan, Victreebel, Ninetales, and Blastoise.
- If the counterpart is Red, his Champion roster uses Let's Go Red's species: Pikachu, Machamp, Arcanine, Lapras, Snorlax, and Venusaur.
- Both counterpart rosters use the reopened League's competitive preparation and dynamic scaling rules.
- Mega Evolution remains disabled for both player and opponents.

## Gym Leader rematches and Trainer Card

- Defeating Professor Oak at Mt. Silver unlocks competitive rematches with all sixteen Kanto and Johto Gym Leaders.
- All rematch teams use competitive builds.
- Defeating all sixteen Gym Leaders in this rematch cycle awards one Trainer Card star.
- Blue's first battle as the reopened Viridian Gym Leader is already his competitive rematch and counts as Viridian's required victory in the sixteen-Leader star cycle; no second Blue victory is required for that star.
- Additional Trainer Card star conditions will be designed separately later.
- After Oak unlocks the rematch system, each of the sixteen Gym Leaders is available once per real-world day using the hardware RTC. First-cycle victories count toward the Trainer Card star; later daily victories award no additional stars.
- A Gym Leader's daily challenge is consumed only when Red wins. Losing allows immediate retries on the same day; after a victory, that Leader resets on the next real-world day.
- All sixteen post-Oak Gym Leader rematch Pokemon are fixed at level 100 with perfect IVs, legal competitive EV spreads, optimized natures, moves and held items, plus maximum AI; these battles do not use dynamic level scaling.
- Every post-Oak Gym Leader rematch uses a full team of six Pokemon.
- All post-Oak Gym Leader rematches use the standard Single Battle format; Double Battle variants are not required.
- The Bag cannot be opened during post-Oak Gym Leader rematches. Held items continue to function normally for both sides.
- Post-Oak Gym Leader rematches respect the player's global Switch/Set battle-style option rather than forcing either mode.
- Post-Oak Gym Leader rematches provide no pre-battle team preview; the opposing team is revealed only as Pokemon enter battle.
- Each Gym Leader uses one fixed, individually designed competitive rematch team. Daily rematches do not rotate or randomize team compositions.
- Gym Leader rematch teams may draw freely from the project's entire obtainable species pool regardless of the Leader's region, provided the selections remain coherent with that Leader's specialization.
- Gym Leader rematch teams use a predominant specialization rule: at least four of the six Pokemon must possess the Leader's characteristic type; up to two off-type Pokemon are permitted when thematically or strategically coherent.
- Remaining secondary decisions concerning competitive team construction use the recommended balanced defaults without requiring a separate owner choice for every detail.

## Johto battle facility

- The Crystal Battle Tower site west of Olivine City is replaced by FireRed/LeafGreen's Seven Island Trainer Tower concept (the Trainer Hill counterpart in Emerald).
- Completing the facility's final challenge awards an Egg containing a baby Pokemon.
- The prize Egg has a 30% probability of being shiny. The result is determined when the Egg is awarded and is not subject to the global 1/4096 wild/breeding shiny rate.
- The baby-Pokemon Egg is awarded after every successful completion, not only the first. Each newly awarded Egg independently rolls the 30% shiny probability.

## Emerald facilities in Johto

- Emerald's Battle Frontier is included as the project's major battle park, adapted to the restricted species pool: Generations I-II plus the permitted later evolutions and baby Pokemon belonging to those families.
- Professor Elm gives the player the pass required to access the Battle Frontier.
- Once unlocked, the Battle Frontier is permanently reachable from both Vermilion City and Olivine City.
- Emerald-style Pokemon Contests are included in Johto.
- The Johto Contest Hall replaces Goldenrod City's Game Corner. NPCs in the Goldenrod underground refer naturally to Contests and the local venue.

## Narrative and canon policy

- The project must resemble an official Generation III Pokemon title in tone, presentation, dialogue length, pacing, and visual language.
- The story remains simple, light, and adventurous. It must not introduce a new villainous team, world-ending threat, prophecy, secret antagonist, forced plot twist, parallel universe, or time-travel plot.
- Team Rocket does not participate in Johto's story.
- Johto is presented as the same region seen in Gold/Silver/Crystal, three years earlier. Changes are communicated through small environmental details and brief NPC dialogue rather than explicit foreshadowing.
- Canonical game continuity is the primary lore reference. Secondary design decisions may be made autonomously; any material change to the supplied narrative or lore requires owner review.
- Catching Raikou, Entei, Suicune, Ho-Oh, or Lugia before the later Gold/Silver events is an explicit gameplay-continuity divergence. The script must not falsely claim that those catches preserve the later games' exact legendary chronology.

## Kanto-to-Johto opening

- After the first Kanto League victory, Red returns to Pallet Town. Leaving the player's house triggers a summons to Professor Oak's Laboratory.
- Oak explains that Kurt sent him the mysterious GS Ball for study. Oak has made progress but cannot fully explain it, so he asks Red to return it to Kurt in Azalea Town.
- Oak frames the journey as a chance for Red to continue improving by challenging Johto's eight Gym Leaders.
- Oak gives Red the GS Ball, the Vermilion-to-Olivine ship ticket, and the Pokegear/Pokenav communication device.
- Oak's number is registered from the beginning. Calling Oak evaluates the player's Pokedex.
- After Battle Frontier access is unlocked, the device gains Emerald-style Frontier information and Symbol tracking.

## S.S. Aqua rival encounter

- The ship is fully explorable and contains cabins, sailors, passengers, and optional Trainer battles.
- Entering the Captain's room starts the first counterpart-rival encounter. The rival is the Captain's eldest child and is traveling to Johto to earn its badges and become Champion.
- The rival challenges the player after learning that the player is Kanto Champion, then promises to achieve the same dream someday.
- The ship reaches Olivine after this scene.
- The rival is competitive but friendly, never cruel or needlessly aggressive, and also introduces Johto history through short, natural dialogue.
- Rival party size progression is fixed by encounter count: three Pokemon aboard the ship, then four, five, and six Pokemon across the three unordered Johto encounters.

## Open Johto, GS Ball, and Celebi

- Johto is broadly open after arrival at Olivine. The first seven Gyms can be completed in any order; Clair is always eighth.
- The player may deliver the GS Ball to Kurt at any time. With zero through six badges, Kurt says that he needs time to compare his knowledge with Oak's research and encourages the player to continue the Gym challenge.
- Earning the seventh Johto badge automatically triggers an Oak call asking whether the GS Ball has been delivered and directing Red back to Kurt.
- If the GS Ball was delivered earlier, Kurt's research is complete on the player's return. If it is first delivered after seven badges, Kurt completes the examination immediately; no artificial waiting period is imposed.
- Kurt concludes that the GS Ball may be linked to Ilex Forest's ancient shrine and returns it to Red.
- The Celebi shrine event requires seven badges, possession of the returned GS Ball, and completion of Kurt's research.
- Red places or uses the GS Ball at the shrine and Celebi appears. Catching Celebi is optional; defeating it does not block progression.
- After the encounter, Kurt gives Red HM Rock Climb. This unlocks the route or puzzle required to reach and complete Clair's Gym.

## Unordered counterpart-rival scenes

- After the ship battle, three independent rival battles occur at the Burned Tower, Lake of Rage, and the Azalea-side entrance to Ilex Forest.
- These three scenes have no required order. Each location has self-contained dialogue, while party size is chosen from the number of prior counterpart battles.
- At Burned Tower, the rival briefly recounts the two towers, the fire, the death of three Pokemon, and Ho-Oh's legendary revival of them as Raikou, Entei, and Suicune.
- Burned Tower's basement is inaccessible, and Eusine does not appear.
- Lake of Rage remains natural: no Red Gyarados and no Team Rocket activity. The rival briefly mentions its history, Gyarados population, and reputation.
- At Ilex Forest, the rival waits at the Azalea entrance in the approximate location of Gold/Silver's rival battle and briefly recounts the shrine legend and the forest protector said to cross time.

## Johto roaming legends

- Raikou, Entei, and Suicune roam appropriate Johto areas from the start of the Johto chapter; this story does not release them from Burned Tower.
- Defeating a roaming beast immediately returns it to the roaming system. Only successful capture permanently removes that individual roamer.

## Johto Gym state three years earlier

- Violet: Falkner is not yet Gym Leader. His traveling father is the official Leader, and Sprout Tower's elder temporarily evaluates challengers. Falkner appears at the Trainer School with a Pidgey. Dialogue may subtly suggest that he could inherit the Gym.
- Olivine: Jasmine is already Gym Leader but currently specializes in Rock-type Pokemon. After defeat she discreetly hints that her interests may be changing toward Steel-type Pokemon.
- Goldenrod: Norman is Gym Leader and uses Normal types. He and his family originate from Johto; after defeat he implies that a distant region has offered him another Gym Leader position. Hoenn is not named directly unless a short natural reference is needed.
- Whitney appears as a young NPC on Goldenrod Department Store's first floor. She likes cute Normal- and Fairy-type Pokemon and has not chosen between them; she is not yet Gym Leader.
- Bugsy, Morty, Chuck, Pryce, and Clair already hold their canonical Gyms.
- Clair is always eighth. After defeat she withholds the badge until Red enters the previously NPC-blocked Dragon's Den and defeats its elder in battle; the elder then awards the eighth badge.

## Johto legendary endgame

- Bell Tower remains inaccessible for the entire adventure, and Ho-Oh is not encountered there.
- The Whirl Islands are initially blocked by NPCs and open only after all eight Johto badges are earned.
- Lugia is absent from its normal Silver-version chamber. An elder there gives Red the key item or ticket that unlocks Navel Rock as a ship destination.
- Navel Rock remains available despite the removal of the rest of the Sevii Islands. Ho-Oh is encountered at its summit and Lugia in its depths.

## Professor Elm and Battle Frontier access

- Professor Elm resides in New Bark Town and recognizes Red because Oak has spoken about the new Kanto Champion.
- Elm's principal endgame function is to give Red the Frontier Pass.
- The Frontier Pass adds the Battle Frontier to the ship destinations available from both Vermilion and Olivine.

## Daily Trainer Tower facility

- The Trainer Tower/Trainer Hill-inspired facility west of Olivine is challengeable once per real-world day.
- Its floor count, modes, opponent builds, intermediate rewards, and baby-Pokemon prize pool are secondary balance decisions to be designed autonomously.
- Completing the daily challenge awards one baby-Pokemon Egg; each award independently has a 30% shiny probability.

## Viridian Gym and Blue

- Viridian Gym reopens with Blue as its Gym Leader.
- Viridian Gym opens only after Professor Oak is defeated at Mt. Silver.
- The reopened Gym contains no subordinate Trainers; only Blue battles the player.
- Blue explains that he was offered the Gym Leader position and has accepted it for now while deciding what to do in the future.
- Blue uses his Let's Go Gym Leader species roster: Tauros, Gyarados, Aerodactyl, Alakazam, Exeggutor, and Charizard. The team receives the project's competitive Gym-rematch preparation and scaling. Charizard cannot Mega Evolve because Mega Evolution is disabled globally.
- Pure trade evolutions evolve when a Link Cable is used from the Bag. Trade-with-held-item evolutions require the Pokemon to hold the correct item and the player to use a Link Cable on it.
- Link Cable evolution consumes the Link Cable. If a held evolution item is also required, that held item is consumed as well. Alternative level-only or held-item-only shortcuts inherited from Heart and Soul are removed for these trade evolution families.
- All permitted evolutions may occur during the Kanto story as soon as their requirements are met; they are not globally locked behind the League.
- Later-generation evolution items are sold at the Goldenrod Department Store in Johto, not in Kanto. Consequently, item-dependent later evolutions remain practically post-League even though the evolution system itself is not globally locked.
- Regional forms connected to Kanto and Johto families, and their regional evolutions, are included.
- Regional forms are obtainable only in the Johto Safari Zone. They do not appear in Kanto or in ordinary Johto encounter tables.
- Bulbasaur, Charmander, and Squirtle are obtainable in separate areas of the Johto Safari Zone at a 10% encounter rate each. Oak's original FireRed starter selection remains unchanged.
- Chikorita, Cyndaquil, and Totodile are obtainable only in separate areas of the Johto Safari Zone at a 10% encounter rate each. Professor Elm does not give Red a Johto starter.
- Kanto trainer parties initially remain faithful to Pokemon FireRed. Any modernization is deferred to a later explicit review.
- Overall Kanto difficulty remains equivalent to Pokemon FireRed.
- Johto access is post-League only.
- Red retains the Kanto party on entering Johto. Johto trainer levels scale dynamically rather than following a single fixed postgame curve.
- Every Johto trainer Pokemon has 31 IVs in all stats and a legal, role-appropriate competitive EV spread totaling 510 EVs (normally 252/252/4), with compatible nature and moves. This applies to ordinary trainers, rivals, Gym Leaders, and other trainer battles, not wild Pokemon.
- Competitive held items are reserved for Johto rivals, Gym Leaders, bosses, and other major opponents. Ordinary trainers retain perfect IVs, competitive EVs, natures, and movesets but are not required to carry optimized held items.
- Johto trainer AI scales upward with Johto badge progression rather than remaining fixed for the whole region.
- Johto ordinary-trainer AI uses three badge tiers: standard at 0-2 badges, intermediate at 3-5, and advanced at 6-8. Rivals, Gym Leaders, bosses, and other major opponents use the next available tier above ordinary trainers, up to the advanced maximum.
- Johto dynamic level scaling uses the highest-level Pokemon in Red's current party at battle start as the reference level.
- Ordinary Johto trainers use `reference level - 5` for their Pokemon.
- Johto Gym Leaders use the exact reference level for their regular team members and `reference level + 3` for their ace. All calculated levels are capped at 100.
- Johto rivals and major story opponents use `reference level - 2` for regular team members and `reference level + 2` for their ace, capped at level 100.
- Johto scaling has a badge-based minimum reference level to prevent lowering opponents by entering with an intentionally underleveled party. The effective reference is the greater of the party's highest level and the current Johto progression floor.
- Johto minimum reference levels by badge progression are `50, 55, 60, 65, 70, 75, 80, 85`. Party-based scaling overrides the floor whenever Red's highest-level party member is above it.
- Ordinary Johto wild Pokemon scale dynamically from `effective reference - 12` through `effective reference - 8`, using the same party-or-badge reference calculation as trainers.
- Johto Safari Zone encounters instead scale from `effective reference - 15` through `effective reference - 10`, including starters and regional forms.
- After the League, Professor Oak gives the player the GS Ball; it must be delivered to Kurt.
- After the first League victory, Professor Oak gives the player both the GS Ball and the S.S. Ticket. The ticket grants access to the S.S. Aqua from Vermilion City to Olivine City; the GS Ball begins the Kurt objective.
- During the initial Kanto story, the Pokedex displays the Kanto section. After the first League victory, Oak automatically upgrades it to the full custom regional Pokedex during the GS Ball/S.S. Ticket event. No 60-caught-species requirement gates the upgrade or Johto access.
- After the first Hall of Fame entry, the Kanto Pokemon League remains closed until Red earns all eight Johto badges (sixteen total). This replaces FireRed's Sevii/Lorelei reopening condition.
- When the League reopens, the Elite Four retain FireRed's original postgame species compositions but receive perfect IVs, legal competitive EV spreads, optimized natures, moves and held items, plus advanced AI. Their levels scale dynamically with an elevated minimum. The Champion is the counterpart rival rather than Blue.
- Reopened League scaling uses an effective reference of at least level 85 or Red's highest party level if higher: Lorelei `reference - 2`, Bruno `reference - 1`, Agatha `reference`, Lance `reference + 1`, Champion regular members `reference + 2`, and Champion ace `reference + 5`, all capped at 100.
- The Kanto-to-Johto connection follows the HGSS model. The current implementation target is the S.S. Aqua route from Vermilion City to Olivine City, gated behind the League and Oak's GS Ball event.
- The unchosen Helix/Dome Fossil is obtainable through a post-League archaeological event in the Ruins of Alph. The original Mt. Moon choice and Kanto dialogue remain unchanged.

## Johto Gym and GS Ball progression

- Johto Gyms 1-7 may be challenged in any order; their teams use the project's dynamic scaling rules.
- Clair is always the eighth Johto Gym Leader.
- Clair's Gym is inaccessible until Red can use Rock Climb.
- Red may deliver the GS Ball to Kurt before earning seven Johto badges. Kurt says that examining it will take time and directs Red to challenge the Johto Gyms in the meantime.
- Earning the seventh Johto badge unlocks the Celebi event in Ilex Forest.
- Completing the Celebi event causes Kurt to grant access to Rock Climb.
- Rock Climb is implemented as a functional field move and is required to reach Clair's Gym.
- The initial Celebi battle completes the Ilex Forest event whether Celebi is caught or defeated.
- If Celebi is defeated, it cannot be challenged again immediately.
- Mt. Silver becomes accessible only after Red holds all sixteen Kanto and Johto badges.
- Professor Oak waits at the summit of Mt. Silver as the final trial.
- Professor Oak uses a full team of six level 100 Pokemon with perfect IVs, legal competitive EV spreads, optimized held items, and maximum AI.
- Defeating Oak unlocks repeatable Celebi rematches by interacting with the Ilex Forest shrine, until Celebi is successfully caught.
- Defeating Oak also awards the Old Sea Map.
- The Old Sea Map permanently unlocks travel to Emerald's Faraway Island from both Vermilion City and Olivine City.
- Faraway Island retains Emerald's map and Mew pursuit event.
- Faraway Island Mew is encountered at level 70 rather than Emerald's original level 30.
- If Mew is defeated or Red runs away, leaving and re-entering the encounter area resets the pursuit event. This remains repeatable until Mew is caught; the Old Sea Map and island access are permanent.

## Decision policy

- Configurable Heart and Soul features are presented to the project owner in small groups before changing their defaults.
- Story, dialogue, map, encounter, and trainer modernization are separate decisions. A gameplay-mechanics choice does not authorize changes to FireRed dialogue.
- Any unavoidable replacement of Sevii-specific dialogue must be documented before it is rewritten.
