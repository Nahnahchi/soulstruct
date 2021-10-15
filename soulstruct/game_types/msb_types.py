from __future__ import annotations

__all__ = [
    "Map",
    "MapTyping",
    "MapEntry",
    "MapEntity",

    "MapModel",
    "MapPieceModel",
    "ObjectModel",
    "CharacterModel",
    "PlayerModel",
    "CollisionModel",
    "NavmeshModel",

    "MapEvent",
    "LightEvent",
    "SoundEvent",
    "VFXEvent",
    "WindEvent",
    "TreasureEvent",
    "SpawnerEvent",
    "MessageEvent",
    "ObjActEvent",
    "SpawnPointEvent",
    "MapOffsetEvent",
    "NavigationEvent",
    "EnvironmentEvent",
    "NPCInvasionEvent",

    "MapPart",
    "MapPiece",
    "Object",
    "Character",
    "Collision",
    "PlayerStart",
    "Navmesh",
    "UnusedObject",
    "UnusedCharacter",
    "MapConnection",

    "Region",
    "RegionVolume",
    "RegionPoint",
    "RegionCircle",
    "RegionSphere",
    "RegionCylinder",
    "RegionRect",
    "RegionBox",

    "MapPartTyping",
    "CoordEntityTyping",
    "ObjectTyping",
    "RegionTyping",
    "CharacterTyping",
    "AnimatedTyping",
    "MapPieceTyping",
    "CollisionTyping",
    "NavigationEventTyping",
]

import typing as tp
from enum import IntEnum, unique

from soulstruct.game_types.basic_types import GameObject
from soulstruct.games import *


class Map(GameObject):
    def __init__(
        self,
        area_id: tp.Optional[int],
        block_id: tp.Optional[int],
        name=None,
        emevd_file_stem=None,
        msb_file_stem=None,
        ai_file_stem=None,
        esd_file_stem=None,
        ffxbnd_file_name=None,
        variable_name=None,
        verbose_name=None,
    ):
        """
        Create a game map instance with associated naming information. These instances can be used as arguments in EVS
        instructions.

        Soulstruct defines constants for existing game maps already, so you shouldn't need to use this class yourself.
        (You can theoretically use transient `Map(a, b)` calls as arguments in EVS instructions, but you may as well
        just use a tuple `(a, b)` in that case, which is also accepted.)

        Args:
            area_id: Area ID of map, which is the first number (of four) in the full map ID. Multiple maps can appear in
                the same area. Some game files (such as lighting parameters) are area-specific rather than map-specific.
            block_id: Block ID of map, which is the second number (of four) in the full map ID. Generally, the area ID
                and block ID fully specify the map. The third number in the map ID is essentially never used and the
                fourth number is only used for file revision purposes (e.g. the Dark Souls DLC version of Darkroot).

            name: Canonical name of map (e.g. "undeadburg"). Note that the map-finding utility `get_map` ignores case
                and underscores when looking for a specific name.

            emevd_file_stem: Name of `emevd` file for this map, without extension.
            msb_file_stem: Name of `msb` file for this map, without extension.
            ai_file_stem: Name of 'luabnd[.dcx]' for this map, without extension(s).
            esd_file_stem: Name of 'talkesdbnd[.dcx]' for this map, without extension(s).

            ffxbnd_file_name: Name of 'ffxbnd[.dcx]' file that Soulstruct should modify for this map. Map areas with
                multiple blocks may have an area-wide file and block-specific files that are both loaded. The block-
                specific files are preferred for ease/efficiency.

            variable_name: Name to use in EVS output (typically upper case with underscores).
            verbose_name: Full descriptive name of map for display in certain output-only fields.

        `name`, `emevd_file_stem`, `msb_file_stem`, `ai_file_stem`, and `esd_file_stem` all default to
        `m{area_id:02d}_{block_id:02d}_00_00` if not specified. `verbose_name` defaults to `name`. `variable_name`
        defaults to None (not a valid EVS instruction argument).
        """
        self.area_id = area_id
        self.block_id = block_id

        base_id = f"m{area_id:02d}_{block_id:02d}_00_00" if area_id is not None and block_id is not None else None
        self.name = base_id if name is None else name

        self.emevd_file_stem = base_id if emevd_file_stem is None else emevd_file_stem
        self.msb_file_stem = base_id if msb_file_stem is None else msb_file_stem
        self.ai_file_stem = base_id if ai_file_stem is None else ai_file_stem
        self.esd_file_stem = base_id if esd_file_stem is None else esd_file_stem
        self.map_load_tuple = (area_id, block_id, -1, -1)  # for `MSBMapConnection`
        self.ffxbnd_file_name = ffxbnd_file_name

        self.variable_name = variable_name
        self.verbose_name = self.name if verbose_name is None else verbose_name

        if self.area_id is not None:
            self.base_entity_id = 100000 * self.area_id + 10000 * self.block_id
            self.flag_prefix = 1000 + 10 * self.area_id + self.block_id

    def stem_set(self):
        return {
            stem
            for stem in (self.emevd_file_stem, self.msb_file_stem, self.ai_file_stem, self.esd_file_stem)
            if stem
        }

    def __eq__(self, other_map: Map):
        return self.area_id == other_map.area_id and self.block_id == other_map.block_id

    def __iter__(self):
        return iter((self.area_id, self.block_id))

    def __repr__(self):
        return self.emevd_file_stem

    @classmethod
    def NO_MAP(cls):
        """Used as a default null map in MSB."""
        return cls(0, 0, name="NONE")


class MapEntry(GameObject):
    """Anything that appears in an MSB."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False) -> [str, str]:
        """Returns the pluralized name of the MSB type (e.g. "Parts") and the non-pluralized name of the subtype
        (e.g. "Character")."""
        raise NotImplementedError

    @classmethod
    def get_msb_class_name(cls) -> str:
        """Returns the name of the Soulstruct MSB class (e.g. "MSBRegionBox").

        By default, this is done by simply prefixing "MSB" to the class name."""
        if cls.__name__ == "MapEntry":
            raise NotImplementedError("MapEntry base class has no corresponding non-abstract MSB class.")
        return f"MSB{cls.__name__}"


@unique
class MapEntity(MapEntry, IntEnum):
    """Any MSB entry with an entity ID (enum values)."""

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False) -> [str, str]:
        raise NotImplementedError

    @classmethod
    def get_id_start_and_max(cls, game: Game) -> tuple[int, int]:
        """Return first and last entity ID value for automatic generation of entity IDs for specific `game`.

        Not supported by default; supported subclasses will override this method.
        """
        raise TypeError(f"`{cls.__name__}` does not use entity IDs.")

    @classmethod
    def auto_generate(cls, count, game: Game, map_range_start: int):
        """Get value for `auto()`.

        Raises `TypeError` if not valid for this class, and `NotImplementedError` if not implemented for given `game`.
        """
        start_value, max_value = cls.get_id_start_and_max(game)
        value = map_range_start + start_value + count
        if value > map_range_start + max_value:
            raise ValueError(f"Too many members in `{cls.__name__}` for `auto()` range `({start_value}, {max_value})`.")
        return value

    # noinspection PyMethodOverriding
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        raise ValueError("Cannot use `auto()` for this `MapEntity` subclass.")


class MapModel(MapEntry):
    """3D model ID of something."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return "Models", None

    @classmethod
    def get_msb_class_name(cls) -> str:
        """All MSB models use the same class."""
        return "MSBModel"


class MapPieceModel(MapModel):
    """Map piece model (e.g. m0000). """
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Models", "MapPieces") if pluralized_subtype else ("Models", "MapPiece")


class ObjectModel(MapModel):
    """Object model (e.g. o0000). """
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Models", "Objects") if pluralized_subtype else ("Models", "Object")


class CharacterModel(MapModel):
    """Character model (e.g. c0000).

    Note that c0000 can appear in either the Characters or Players parts list in an MSB.
    """
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Models", "Characters") if pluralized_subtype else ("Models", "Character")


class PlayerModel(MapModel):
    """Sometimes c0000 is registered as this type instead of a CharacterModel."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Models", "Players") if pluralized_subtype else ("Models", "Player")


class CollisionModel(MapModel):
    """Map piece model (e.g. h0000). """
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Models", "Collisions") if pluralized_subtype else ("Models", "Collision")


class NavmeshModel(MapModel):
    """Navmesh model (e.g. n0000). """
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Models", "Navmeshes") if pluralized_subtype else ("Models", "Navmesh")


class MapEvent(MapEntity):
    """Base class for things that appear in the 'events' section of the MSB, such as sounds, ObjActs, and VFX."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return "Events", None

    def auto_region_name(self):
        event_enum_subclass = self.__class__.__bases__[0]
        while event_enum_subclass.__bases__[0] is not MapEvent:
            event_enum_subclass = event_enum_subclass.__bases__[0]
        return f"_{event_enum_subclass.__name__}_{self.name.lstrip('_')}"


class LightEvent(MapEvent):
    """Light event in MSB."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "Lights") if pluralized_subtype else ("Events", "Light")


class SoundEvent(MapEvent):
    """Sound event in MSB attached to a Region (a 'map sound'), which can be enabled or disabled.

    Note that these are enabled on map load, so you may want to disable it (e.g. boss music) in your constructor event.
    """

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "Sounds") if pluralized_subtype else ("Events", "Sound")

    @classmethod
    def get_id_start_and_max(cls, game: Game) -> tuple[int, int]:
        if game in (DARK_SOULS_PTDE, DARK_SOULS_DSR):
            return 3800, 3899
        raise NotImplementedError(f"Entity ID range not implemented for {game.name}.")


class VFXEvent(MapEvent):
    """VFX event (visual effect, e.g. fog gate) in MSB attached to a region.

    Can be created or deleted. When deleted, the particles already emitted can be allowed to live out their remaining
    life (`erase_root_only=True` by default).
    """

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "VFX") if pluralized_subtype else ("Events", "VFX")

    @classmethod
    def get_id_start_and_max(cls, game: Game) -> tuple[int, int]:
        if game in (DARK_SOULS_PTDE, DARK_SOULS_DSR):
            return 3400, 3599
        raise NotImplementedError(f"Entity ID range not implemented for {game.name}.")


class WindEvent(MapEvent):
    """Wind event in MSB."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "Wind") if pluralized_subtype else ("Events", "Wind")


class TreasureEvent(MapEvent):
    """Treasure event in MSB."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "Treasure") if pluralized_subtype else ("Events", "Treasure")


class SpawnerEvent(MapEvent):
    """Spawner event (causes linked enemies to respawn) in MSB attached to a region. Can be enabled or disabled."""

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "Spawners") if pluralized_subtype else ("Events", "Spawner")

    @classmethod
    def get_id_start_and_max(cls, game: Game) -> tuple[int, int]:
        if game in (DARK_SOULS_PTDE, DARK_SOULS_DSR):
            return 3600, 3699
        raise NotImplementedError(f"Entity ID range not implemented for {game.name}.")


class MessageEvent(MapEvent):
    """Message event in MSB that causes a "developer message" to appear in a region. Can be enabled or disabled."""

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "Messages") if pluralized_subtype else ("Events", "Message")

    @classmethod
    def get_id_start_and_max(cls, game: Game) -> tuple[int, int]:
        if game in (DARK_SOULS_PTDE, DARK_SOULS_DSR):
            return 3700, 3799
        raise NotImplementedError(f"Entity ID range not implemented for {game.name}.")


class ObjActEvent(MapEvent):
    """ObjAct (object activation event) added in MSB.

    It can be used in conditions as a test for the ObjAct event being triggered.
    """
    def __call__(self, negate=False, condition=None, skip_lines=0):
        from soulstruct.base.events.emevd.utils import get_value_test
        from soulstruct.base.events.emevd import instructions as instr

        try:
            value = self.value
        except AttributeError:
            value = self
        return get_value_test(
            value=value, negate=negate, condition=condition, skip_lines=skip_lines, if_true_func=instr.IfObjectActivated
        )

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "ObjActs") if pluralized_subtype else ("Events", "ObjAct")

    @classmethod
    def get_id_start_and_max(cls, game: Game) -> tuple[int, int]:
        raise TypeError("`ObjActEvent` does not use normal entity IDs, but uses special flags instead.")


class SpawnPointEvent(MapEvent):
    """Spawn point attached to an MSB region."""

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "SpawnPoints") if pluralized_subtype else ("Events", "SpawnPoint")

    @classmethod
    def get_id_start_and_max(cls, game: Game) -> tuple[int, int]:
        if game in (DARK_SOULS_PTDE, DARK_SOULS_DSR):
            return 3900, 3949  # 3950-3989 reserved for bonfire spawn points
        raise NotImplementedError(f"Entity ID range not implemented for {game.name}.")


class MapOffsetEvent(MapEvent):
    """Map offset event in MSB."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "MapOffsets") if pluralized_subtype else ("Events", "MapOffset")


class NavigationEvent(MapEvent):
    """Event attached to an MSB navmesh part.

    Enable/disable/toggle functions require you to specify a navigation type; only the flags for that type will be
    modified in the navmesh.
    """

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "Navigation") if pluralized_subtype else ("Events", "Navigation")

    @classmethod
    def get_id_start_and_max(cls, game: Game) -> tuple[int, int]:
        raise TypeError(
            "Navigation entity IDs are also baked into navmesh NVM geometry, so automatic enumeration is not yet "
            "supported."
        )
        # return 4000, 4199


class EnvironmentEvent(MapEvent):
    """Environment event in MSB."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "Environments") if pluralized_subtype else ("Events", "Environment")


class NPCInvasionEvent(MapEvent):
    """Event describing invasion of NPC's world (e.g. Lautrec) in MSB."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "NPCInvasion") if pluralized_subtype else ("Events", "NPCInvasion")


class Region(MapEntity):
    """Condition upon a region as a shortcut to condition upon the player being inside it (condition only)."""

    def __call__(self, negate=False, condition=None, skip_lines=0):
        from soulstruct.base.events.emevd.utils import get_value_test
        from soulstruct.base.events.emevd import instructions as instr

        try:
            value = self.value
        except AttributeError:
            value = self
        return get_value_test(
            value=value,
            negate=negate,
            condition=condition,
            skip_lines=skip_lines,
            if_true_func=instr.IfPlayerInsideRegion,
            if_false_func=instr.IfPlayerOutsideRegion,
        )

    @classmethod
    def get_coord_entity_type(cls):
        from soulstruct.base.events.emevd.enums import CoordEntityType

        return CoordEntityType.Region

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return "Regions", None


class RegionVolume(Region):
    """Soulstruct ABC for Spheres, Cylinders, and Boxes, which share an auto-enumeration schema separate from Points."""

    @classmethod
    def get_id_start_and_max(cls, game: Game) -> tuple[int, int]:
        if game in (DARK_SOULS_PTDE, DARK_SOULS_DSR):
            return 2000, 2499
        raise NotImplementedError(f"Entity ID range not implemented for {game.name}.")


class RegionPoint(Region):
    """Single point region."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Regions", "Points") if pluralized_subtype else ("Regions", "Point")

    @classmethod
    def get_id_start_and_max(cls, game: Game) -> tuple[int, int]:
        if game in (DARK_SOULS_PTDE, DARK_SOULS_DSR):
            return 2500, 2899
        raise NotImplementedError(f"Entity ID range not implemented for {game.name}.")


class RegionCircle(Region):
    """2D circle region. Never used."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Regions", "Circles") if pluralized_subtype else ("Regions", "Circle")


class RegionSphere(RegionVolume):
    """3D spherical region."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Regions", "Spheres") if pluralized_subtype else ("Regions", "Sphere")


class RegionCylinder(RegionVolume):
    """3D cylindrical region."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Regions", "Cylinders") if pluralized_subtype else ("Regions", "Cylinder")


class RegionRect(Region):
    """2D rectangular region. Never used."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Regions", "Rects") if pluralized_subtype else ("Regions", "Rect")


class RegionBox(RegionVolume):
    """3D box region."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Regions", "Boxes") if pluralized_subtype else ("Regions", "Box")


class MapPart(MapEntity):
    """Base class for anything that appears in the Parts section of the MSB."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return "Parts", None


class MapPiece(MapPart):
    """Map Piece added in MSB."""

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Parts", "MapPieces") if pluralized_subtype else ("Parts", "MapPiece")

    @classmethod
    def get_id_start_and_max(cls, game: Game) -> tuple[int, int]:
        if game in (DARK_SOULS_PTDE, DARK_SOULS_DSR):
            return 3000, 3199
        raise NotImplementedError(f"Entity ID range not implemented for {game.name}.")


class Object(MapPart):
    """Condition upon an object as a shortcut to condition upon it *not* being destroyed."""

    def __call__(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        from soulstruct.base.events.emevd.utils import get_value_test
        from soulstruct.base.events.emevd import instructions as instr

        try:
            value = self.value
        except AttributeError:
            value = self
        return get_value_test(
            value=value,
            negate=negate,
            condition=condition,
            skip_lines=skip_lines,
            end_event=end_event,
            restart_event=restart_event,
            skip_if_true_func=instr.SkipLinesIfObjectNotDestroyed,
            skip_if_false_func=instr.SkipLinesIfObjectDestroyed,
            if_true_func=instr.IfObjectNotDestroyed,
            if_false_func=instr.IfObjectDestroyed,
            end_if_true_func=instr.EndIfObjectNotDestroyed,
            end_if_false_func=instr.EndIfObjectDestroyed,
            restart_if_true_func=instr.RestartIfObjectNotDestroyed,
            restart_if_false_func=instr.RestartIfObjectDestroyed,
        )

    @classmethod
    def get_coord_entity_type(cls):
        from soulstruct.base.events.emevd.enums import CoordEntityType

        return CoordEntityType.Object

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Parts", "Objects") if pluralized_subtype else ("Parts", "Object")

    @classmethod
    def get_id_start_and_max(cls, game: Game) -> tuple[int, int]:
        """Note that range 1900-1999 is reserved for special manual assignment (bonfires, fog objects, fog VFX)."""
        if game in (DARK_SOULS_PTDE, DARK_SOULS_DSR):
            return 1000, 1899
        raise NotImplementedError(f"Entity ID range not implemented for {game.name}.")


class Character(MapPart):
    """Condition upon a character as a shortcut to condition upon them being alive."""

    def __call__(self, negate=False, condition=None, skip_lines=0):
        from soulstruct.base.events.emevd.utils import get_value_test
        from soulstruct.base.events.emevd import instructions as instr

        try:
            value = self.value
        except AttributeError:
            value = self
        return get_value_test(
            value=value,
            negate=negate,
            condition=condition,
            skip_lines=skip_lines,
            if_true_func=instr.IfCharacterAlive,
            if_false_func=instr.IfCharacterDead,
        )

    @classmethod
    def get_coord_entity_type(cls):
        from soulstruct.base.events.emevd.enums import CoordEntityType

        return CoordEntityType.Character

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Parts", "Characters") if pluralized_subtype else ("Parts", "Character")

    @classmethod
    def get_id_start_and_max(cls, game: Game) -> tuple[int, int]:
        """Note that range 0900-0999 is reserved for special manual assignment (bonfire characters)."""
        if game in (DARK_SOULS_PTDE, DARK_SOULS_DSR):
            return 0, 899
        raise NotImplementedError(f"Entity ID range not implemented for {game.name}.")


class PlayerStart(MapPart):
    """PlayerStart added in MSB. Used as an argument in `Warp` instructions. No additional state."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Parts", "PlayerStarts") if pluralized_subtype else ("Parts", "PlayerStart")

    @classmethod
    def get_id_start_and_max(cls, game: Game) -> tuple[int, int]:
        if game in (DARK_SOULS_PTDE, DARK_SOULS_DSR):
            return 990, 999
        raise NotImplementedError(f"Entity ID range not implemented for {game.name}.")


class Collision(MapPart):
    """Collision added in MSB."""

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Parts", "Collisions") if pluralized_subtype else ("Parts", "Collision")

    @classmethod
    def get_id_start_and_max(cls, game: Game) -> tuple[int, int]:
        if game in (DARK_SOULS_PTDE, DARK_SOULS_DSR):
            return 3200, 3399
        raise NotImplementedError(f"Entity ID range not implemented for {game.name}.")


class Navmesh(MapPart):
    """Navmesh instance. NavmeshEvents are attached to it and manipulated with EMEVD."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Parts", "Navmeshes") if pluralized_subtype else ("Parts", "Navmesh")


class UnusedObject(MapPart):
    """Unused (or cutscene-only) object in MSB."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Parts", "UnusedObjects") if pluralized_subtype else ("Parts", "UnusedObject")


class UnusedCharacter(MapPart):
    """Unused (or cutscene-only) character in MSB."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Parts", "UnusedCharacters") if pluralized_subtype else ("Parts", "UnusedCharacter")


class MapConnection(MapPart):
    """MapConnection added in MSB. No additional state."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Parts", "MapConnections") if pluralized_subtype else ("Parts", "MapConnection")


MapTyping = tp.Union[Map, tuple, list]
MapPartTyping = tp.Union[MapPart, int]
CoordEntityTyping = tp.Union[Object, Region, Character, int]
ObjectTyping = tp.Union[Object, int]
RegionTyping = tp.Union[Region, int]
CharacterTyping = tp.Union[Character, int]
AnimatedTyping = tp.Union[Character, Object, int]
MapPieceTyping = tp.Union[MapPiece, int]
CollisionTyping = tp.Union[Collision, int]
NavigationEventTyping = tp.Union[NavigationEvent, int]
# TODO: More.
