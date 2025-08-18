import pydantic
import typing
import logging
import pathlib

TData = typing.TypeVar("TData")

# ---------------------------------------------------------
# Message type constants
# ---------------------------------------------------------
class MessageType:
    A: int = 0
    B: int = 1
    C: int = 2
    D: int = 3


# ---------------------------------------------------------
# Base message classes
# ---------------------------------------------------------
class BaseMessage(pydantic.BaseModel, typing.Generic[TData]):
    id: str
    from_id: str
    to_id: str
    type: int
    data: TData


class AMessage(BaseMessage[str]):
    type: int = MessageType.A


class BMessage(BaseMessage[dict[str, typing.Any]]):
    type: int = MessageType.B
    has: str


class CMessage(BaseMessage[list[str]]):
    type: int = MessageType.C


class DMessage(BaseMessage[list[dict[str, typing.Any]]]):
    type: int = MessageType.D
    path: pathlib.Path

# ---------------------------------------------------------
# Config
# ---------------------------------------------------------
class ConfigModel(pydantic.BaseModel):
    logger: logging.Logger

    model_config = pydantic.ConfigDict(arbitrary_types_allowed=True)


# ---------------------------------------------------------
# Chain of Responsibility base
# ---------------------------------------------------------
class MessageHandler:
    def __init__(self, next_handler: typing.Self|None = None):
        self._next = next_handler

    def set_next(self, handler: "MessageHandler") -> "MessageHandler":
        self._next = handler
        return handler

    def handle(self, raw: dict, config: ConfigModel) -> BaseMessage:
        result = self._process(raw, config)
        if result is not None:
            return result
        if self._next:
            return self._next.handle(raw, config)
        return BaseMessage(**raw)  # Fallback to base

    def _process(self, raw: dict, config: ConfigModel) -> typing.Optional[BaseMessage]:
        """Try to create a message. Return None if not possible."""
        raise NotImplementedError


# ---------------------------------------------------------
# Concrete handlers
# ---------------------------------------------------------
class AMessageHandler(MessageHandler):
    def _process(self, raw: dict, config: ConfigModel): -> Those handler all require the same config -> is there any deisign more professional
        if raw.get("type") == MessageType.A:
            try:
                return AMessage(**raw)
            except pydantic.ValidationError as e:
                config.logger.error(f"AMessage validation error: {e}")
        return None


class BMessageHandler(MessageHandler):
    def _process(self, raw: dict, config: ConfigModel):
        if raw.get("type") == MessageType.B:
            try:
                return BMessage(**raw)
            except pydantic.ValidationError as e:
                config.logger.error(f"BMessage validation error: {e}")
        return None


class CMessageHandler(MessageHandler):
    def _process(self, raw: dict, config: ConfigModel):
        if raw.get("type") == MessageType.C:
            try:
                return CMessage(**raw)
            except pydantic.ValidationError as e:
                config.logger.error(f"CMessage validation error: {e}")
        return None


class DMessageHandler(MessageHandler):
    def _process(self, raw: dict, config: ConfigModel):
        if raw.get("type") == MessageType.D:
            try:
                return DMessage(**raw)
            except pydantic.ValidationError as e:
                config.logger.error(f"DMessage validation error: {e}")
        return None


# ---------------------------------------------------------
# Factory to build the handler chain
# ---------------------------------------------------------
def build_message_handler_chain() -> MessageHandler:
    a = AMessageHandler()
    b = BMessageHandler()
    c = CMessageHandler()
    d = DMessageHandler()

    a.set_next(b) \
     .set_next(c) \
     .set_next(d)
    return a

def clean_message(raw_message:dict, config:ConfigModel, to_obj:bool=True) -> dict[str, typing.Any]|BaseMessage:
    handler_chain = build_message_handler_chain()
    clean_message = handler_chain.handle(raw_message, config)
    return clean_message.model_dump(exclude_none=True) if to_obj else clean_message


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    logger = logging.getLogger("message_chain")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    config = ConfigModel(logger=logger)

    raw_message = {
        "id": "123",
        "from_id": "u1",
        "to_id": "u2",
        "type": MessageType.B,
        "data": {"hello": "world"},
        "has": "extra"
    }

    msg = clean_message(raw_message, config)
    print(msg)
