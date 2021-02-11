import jsonpickle
from datetime import datetime, timezone
from ppmpmessage.v3.device_state import DeviceState
from ppmpmessage.v3.message_payload import MessagePayload
from ppmpmessage.v3.message import Message
from ppmpmessage.v3.measurement_payload import MeasurementPayload

def local_now():
    """The current timestamp in UTC timezone."""
    return datetime.now(timezone.utc).astimezone().isoformat()

def dumps(data, **kwargs):
    """Convert a PPMP entity to JSON. Additional arguments are the same as
    accepted by `json.dumps`."""
    return jsonpickle.encode(data, unpicklable=False)

def fletcher16(data):
    """ Generate Fletcher16 hash

    Arguments:
        string {str} -- Input to hash

    Returns:
        [str] -- Fletcher16 output
    """
    sum1, sum2 = 0, 0

    for elem in (ord(x) for x in data):
        sum1 = (sum1 + elem) % 255
        sum2 = (sum2 + sum1) % 255

    return str(hex((sum2 << 8) | sum1)).replace("0x", "").upper()

def machine_message_generator(device, state=DeviceState.OK, code="online"):
    setattr(device, "state", state)

    return dumps(
        MessagePayload(
            device,
            Message(local_now(), code=code)
        ).to_ppmp()
    )

def measurement_payload_generator(device, measurements):
    return dumps(
        MeasurementPayload(
            device,
            measurements
        ).to_ppmp()
    )
