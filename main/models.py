from django.db import models
from django.utils import timezone
from django.conf import settings


class TestCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='название категории')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class LabTest(models.Model):
    name = models.CharField(max_length=100, verbose_name='название анализа')
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE,
                                 verbose_name='категория',
                                 null=True, blank=True)
    description = models.TextField(verbose_name='описание',
                                   null=True, blank=True)
    price = models.IntegerField(verbose_name='цена',
                                null=True, blank=True)
    time = models.IntegerField(verbose_name='срок выполнения',
                               null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Анализ'
        verbose_name_plural = 'Анализы'
        ordering = ('name',)


class Doctor(models.Model):
    PRIMARY_VISIT = 'первичный прием'
    SECONDARY_VISIT = 'повторный прием'

    VISITS = (
        (PRIMARY_VISIT, 'первичный прием'),
        (SECONDARY_VISIT, 'повторный прием')

    )
    specialization = models.CharField(max_length=100,
                                      verbose_name='специализация')
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE,
                                 verbose_name='категория', null=True,
                                 blank=True)
    price = models.IntegerField(verbose_name='цена', null=True, blank=True)
    visit = models.CharField(max_length=20, choices=VISITS)

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'
        ordering = ('specialization',)

    def __str__(self):
        return f'{self.specialization}'


class Booking(models.Model):
    TIMESLOT_LIST = (
        (0, '09:00 – 09:30'),
        (1, '10:00 – 10:30'),
        (2, '11:00 – 11:30'),
        (3, '12:00 – 12:30'),
        (4, '13:00 – 13:30'),
        (5, '14:00 – 14:30'),
        (6, '15:00 – 15:30'),
        (7, '16:00 – 16:30'),
        (8, '17:00 – 17:30'),
    )
    date = models.DateField(default=timezone.now, verbose_name='дата')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,
                               verbose_name='доктор')
    timeslot = models.IntegerField(choices=TIMESLOT_LIST,
                                   verbose_name='время приема')
    is_booked = models.BooleanField(default=False,
                                    verbose_name='забронировано')
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                verbose_name='пациент',
                                null=True, blank=True)

    def __str__(self):
        return (f'Доктор:{self.doctor}, '
                f'пациент {self.patient} время приема {self.timeslot}')

    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]

    class Meta:
        verbose_name = 'Время приема'
        verbose_name_plural = 'Время приема'
