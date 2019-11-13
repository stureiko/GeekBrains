import sys
import ctypes
import struct

a = 5
b = 125.4
c = 'Hello moo'

# адрес объекта
print(id(a))
print(sys.getsizeof(a))
print(ctypes.string_at(id(a), sys.getsizeof(a)))
print(struct.unpack('llli', ctypes.string_at(id(a), sys.getsizeof(a))))

print('*' * 50)

print(id(b))
print(sys.getsizeof(b))
print(ctypes.string_at(id(b), sys.getsizeof(b)))
print(struct.unpack('LLd', ctypes.string_at(id(b), sys.getsizeof(b))))