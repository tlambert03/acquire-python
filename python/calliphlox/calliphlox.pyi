from typing import (
    Any,
    ClassVar,
    Dict,
    Iterator,
    List,
    Optional,
    Tuple,
    final,
    overload,
)
from numpy.typing import NDArray

@final
class AvailableData:
    def frames(self) -> Iterator[VideoFrame]: ...
    def get_frame_count(self) -> int: ...
    def __iter__(self) -> Iterator[VideoFrame]: ...

@final
class Camera:
    identifier: Optional[DeviceIdentifier]
    settings: CameraProperties
    def __init__(self, *args:None, **kwargs: Any) -> None: ...
    def dict(self) -> Dict[str, Any]: ...

@final
class CameraProperties:
    exposure_time_us: float
    line_interval_us: float
    binning: float
    pixel_type: SampleType
    readout_direction: Direction
    offset: Tuple[int, int]
    shape: Tuple[int, int]
    triggers: List[Trigger]
    def __init__(self, *args:None, **kwargs: Any) -> None: ...
    def dict(self) -> Dict[str, Any]: ...

@final
class Channel:
    display_name: str
    line: int
    sample_type: SampleType
    signal_io_kind: SignalIOKind
    signal_type: SignalType
    voltage_range: VoltageRange
    def __init__(self, *args:None, **kwargs: Any) -> None: ...
    def dict(self) -> Dict[str, Any]: ...

@final
class DeviceIdentifier:
    id: Tuple[int, int]
    kind: DeviceKind
    name: str
    def __init__(self, *args:None, **kwargs: Any) -> None: ...
    def dict(self) -> Dict[str, Any]: ...
    @staticmethod
    def none() -> DeviceIdentifier: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

@final
class DeviceKind:
    Camera: ClassVar[DeviceKind] = ...
    NONE: ClassVar[DeviceKind] = ...
    Signals: ClassVar[DeviceKind] = ...
    StageAxis: ClassVar[DeviceKind] = ...
    Storage: ClassVar[DeviceKind] = ...
    def __init__(self, *args:None, **kwargs: Any) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

@final
class DeviceManager:
    def devices(self) -> List[DeviceIdentifier]: ...
    @overload
    def select(
        self, kind: DeviceKind
    ) -> Optional[DeviceIdentifier]: ...
    @overload
    def select(
        self, kind: DeviceKind, name: Optional[str]
    ) -> Optional[DeviceIdentifier]: ...
    def select_one_of(
        self, kind: DeviceKind, names: List[str]
    ) -> Optional[DeviceIdentifier]: ...

@final
class DeviceState:
    Closed: ClassVar[DeviceState] = ...
    AwaitingConfiguration: ClassVar[DeviceState] = ...
    Armed: ClassVar[DeviceState] = ...
    Running: ClassVar[DeviceState] = ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

@final
class Direction:
    Backward: ClassVar[Direction] = ...
    Forward: ClassVar[Direction] = ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

@final
class PID:
    derivative: float
    integral: float
    proportional: float
    def __init__(self, *args:None, **kwargs: Any) -> None: ...
    def dict(self) -> Dict[str, Any]: ...

@final
class Properties:
    signals: Signals
    stages: Tuple[StageAxis, StageAxis, StageAxis]
    video: Tuple[VideoStream, VideoStream]
    def __init__(self, *args:None, **kwargs: Any) -> None: ...
    def dict(self) -> Dict[str, Any]: ...

@final
class Runtime:
    def __init__(self, *args:None, **kwargs: Any) -> None: ...
    def device_manager(self) -> DeviceManager: ...
    def get_available_data(self, stream_id: int) -> AvailableData: ...
    def get_configuration(self) -> Properties: ...
    def get_state(self) -> DeviceState: ...
    def set_configuration(self, properties: Properties) -> Properties: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...

@final
class SampleRateHz:
    numerator: int
    denominator: int
    def __init__(self, *args:None, **kwargs: Any) -> None: ...
    def dict(self) -> Dict[str, Any]: ...

@final
class SampleType:
    F32: ClassVar[SampleType] = ...
    I16: ClassVar[SampleType] = ...
    I8: ClassVar[SampleType] = ...
    U16: ClassVar[SampleType] = ...
    U8: ClassVar[SampleType] = ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

@final
class Signals:
    identifier: Optional[DeviceIdentifier]
    settings: SignalProperties
    def dict(self) -> Dict[str, Any]: ...
@final
class SignalIOKind:
    Input: ClassVar[SignalIOKind] = ...
    Output: ClassVar[SignalIOKind] = ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

@final
class SignalProperties:
    channels: List[Channel]
    timing: Timing
    Trigger: List[Trigger]
    def __init__(self, *args:None, **kwargs: Any) -> None: ...
    def dict(self) -> Dict[str, Any]: ...

@final
class SignalType:
    Analog: ClassVar[SignalType] = ...
    Digital: ClassVar[SignalType] = ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

@final
class StageAxis:
    identifier: Optional[DeviceIdentifier]
    settings: StageAxisProperties
    def dict(self) -> Dict[str, Any]: ...

@final
class StageAxisProperties:
    feedback: PID
    immediate: StageAxisState
    target: StageAxisState
    def dict(self) -> Dict[str, Any]: ...

@final
class StageAxisState:
    position: float
    velocity: float
    def dict(self) -> Dict[str, Any]: ...

@final
class Storage:
    identifier: Optional[DeviceIdentifier]
    settings: StorageProperties
    def dict(self) -> Dict[str, Any]: ...

@final
class StorageProperties:
    filename: None | str
    first_frame_id: int
    def dict(self) -> Dict[str, Any]: ...

@final
class Timing:
    terminal: int
    edge: TriggerEdge
    samples_per_second: SampleRateHz
    def __init__(self, *args:None, **kwargs: Any) -> None: ...
    def dict(self) -> Dict[str, Any]: ...

@final
class Trigger:
    enable: bool
    line: int
    event: TriggerEvent
    kind: SignalIOKind
    edge: TriggerEdge
    def __init__(self, *args:None, **kwargs: Any) -> None: ...
    def dict(self) -> Dict[str, Any]: ...

@final
class TriggerEdge:
    Falling: ClassVar[TriggerEdge] = ...
    NotApplicable: ClassVar[TriggerEdge] = ...
    Rising: ClassVar[TriggerEdge] = ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

@final
class TriggerEvent:
    AcquisitionStart: ClassVar[TriggerEvent] = ...
    Exposure: ClassVar[TriggerEvent] = ...
    FrameStart: ClassVar[TriggerEvent] = ...
    FrameTriggerWait: ClassVar[TriggerEvent] = ...
    Unknown: ClassVar[TriggerEvent] = ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

@final
class VideoFrame:
    def data(self) -> NDArray[Any]: ...
    def metadata(self) -> VideoFrameMetadata: ...

@final
class VideoFrameMetadata:
    frame_id: int
    timestamps: VideoFrameTimestamps
    def dict(self) -> Dict[str, Any]: ...

@final
class VideoFrameTimestamps:
    hardware: int
    acq_thread: int
    def dict(self) -> Dict[str, Any]: ...

@final
class VideoStream:
    camera: Camera
    storage: Storage
    max_frame_count: int
    frame_average_count: int
    def dict(self) -> Dict[str, Any]: ...

@final
class VoltageRange:
    mn: float
    mx: float
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, mn: float, mx: float) -> None: ...
    def dict(self) -> Dict[str, float]: ...

def core_api_version() -> str: ...
