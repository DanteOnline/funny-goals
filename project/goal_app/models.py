from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    in_future = models.BooleanField(default=False)
    in_future_reason = models.TextField(blank=True)
    priority = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["priority"]

    def __str__(self):
        return self.name


class Goal(models.Model):
    name = models.CharField(max_length=64)
    is_success = models.BooleanField(default=False)
    in_control = models.BooleanField(default=False)
    refs_in_control = models.ManyToManyField('self', null=True, blank=True)
    is_personal = models.BooleanField(default=False)

    def has_refs_in_control(self):
        return self.in_control or bool(self.refs_in_control.all())

    def get_refs_in_control(self):
        return self.refs_in_control.all()

    TODAY = 'TD'
    SHORT = 'SH'
    MIDDLE = 'MD'
    LONG = 'LG'

    BY_TIME = (
        (TODAY, 'На сегодня'),
        (SHORT, 'Краткосрочные'),
        (MIDDLE, 'Среднесрочные'),
        (LONG, 'Долгострочные')
    )

    by_time = models.CharField(max_length=2, choices=BY_TIME)

    RESULT = 'R'
    PROCESS = 'P'

    BY_TYPE = (
        (RESULT, 'На результат'),
        (PROCESS, 'На процесс')
    )

    by_type = models.CharField(max_length=1, choices=BY_TYPE)

    def get_type(self):
        for t in self.BY_TYPE:
            if t[0] == self.by_type:
                return t[1]

    why_important = models.TextField(blank=True)
    category = models.ForeignKey(Category)

    def __str__(self):
        return '({}) {}'.format(self.in_control, self.name)
