import asyncio
import logging

_LOGGER = logging.getLogger(__name__)

class PHDController:
    def __init__(self, host, port=23, debug=False):
        self.host = host
        self.port = int(port) if port else 23
        self.debug = debug

    async def send_command(self, cmd: str, timeout: float = 2.0):
        if not self.host:
            raise ValueError('Host not configured')
        try:
            reader, writer = await asyncio.open_connection(self.host, self.port)
            message = cmd + '\r\n'
            if self.debug:
                _LOGGER.debug('Sending to %s:%s -> %s', self.host, self.port, message.strip())
            writer.write(message.encode('utf-8'))
            await writer.drain()
            # short read attempt for any response
            try:
                data = await asyncio.wait_for(reader.read(512), timeout=0.5)
                resp = data.decode('utf-8', errors='ignore').strip() if data else ''
                if self.debug:
                    _LOGGER.debug('Received response: %s', resp)
            except asyncio.TimeoutError:
                resp = ''
                if self.debug:
                    _LOGGER.debug('No response received (timeout)')
            try:
                writer.close()
                await writer.wait_closed()
            except Exception:
                pass
            return resp
        except Exception as e:
            _LOGGER.error('Send failed to %s:%s -> %s', self.host, self.port, e)
            raise
