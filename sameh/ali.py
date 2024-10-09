import pygame
import sys

def start_game():
    # تهيئة Pygame
    pygame.init()

    # إعداد النافذة
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('نافذة بسيطة باستخدام Pygame')

    # إعداد ألوان
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    # إعداد المتغيرات
    x, y = 300, 200  # إحداثيات الدائرة
    radius = 20  # نصف قطر الدائرة
    speed_x, speed_y = 3, 3  # سرعة الحركة

    # حلقة اللعبة
    while True:
        # معالجة الأحداث
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # تحريك الدائرة
        x += speed_x
        y += speed_y

        # منع الدائرة من الخروج من حدود النافذة
        if x - radius < 0 or x + radius > 600:
            speed_x = -speed_x
        if y - radius < 0 or y + radius > 400:
            speed_y = -speed_y

        # رسم العناصر
        screen.fill(WHITE)  # ملء الشاشة باللون الأبيض
        pygame.draw.circle(screen, RED, (x, y), radius)  # رسم الدائرة

        # تحديث الشاشة
        pygame.display.flip()

        # تأخير صغير لزيادة التحكم في سرعة الحركة
        pygame.time.delay(20)
