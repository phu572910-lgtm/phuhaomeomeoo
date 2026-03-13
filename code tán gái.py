import random

ten = input("Tên của bạn: ")
thich = input("Bạn thích điều gì: ")
no = input("Bạn đang ở đâu: ")

loi_tinh = [
f"""
{ten} à,

Giữa thế giới rộng lớn này,
mình lại chú ý đến một điều rất nhỏ:
đó là bạn thích {thich}.

Không biết ở {no},
có ngày nào mình được cùng bạn
đi dạo, trò chuyện
và cùng nhau tận hưởng
những điều giản dị đó không?
""",

f"""
{ten},

Nghe nói bạn thích {thich}.
Tự nhiên mình nghĩ rằng,
nếu một ngày nào đó ở {no},
hai người cùng thích một điều giống nhau
thì chắc cũng thú vị lắm.

Mình chỉ muốn nói rằng
gửi link này cho bạn
không phải là ngẫu nhiên.
""",

f"""
{ten} thân mến,

Ở {no} chắc có nhiều điều đẹp,
nhưng mình đoán
điều làm bạn vui nhất
có lẽ vẫn là {thich}.

Nếu có dịp,
mình cũng muốn được cùng bạn
trải nghiệm điều đó.
"""
]

print("\n--- Tin nhắn dành cho bạn ---\n")
print(random.choice(loi_tinh))
