from django.db import models

from user.models import User


class HostedApp(models.Model):
    RUN = "RUN"
    STOP = "STOP"
    DELETE = 'DELETE'
    RESTART = "RESTART"

    STATUSES = (
        (RUN, "Run"),
        (STOP, "Stop"),
        (DELETE, "Delete"),
        (RESTART, "Restart"),
    )
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', blank=True)
    docker_container_id = models.CharField('ID контейнера', max_length=100, blank=True)
    created_at = models.DateTimeField('Время создания', auto_now_add=True)
    updated_at = models.DateTimeField('Время обновления', auto_now=True)
    started_at = models.DateTimeField('Время запуска', auto_now=True)

    status = models.CharField(
        verbose_name="Статус приложения",
        max_length=20,
        choices=STATUSES,
        default=STOP,
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='user')

    class Meta:
        verbose_name = "Приложение"
        verbose_name_plural = "Приложения"

    def __str__(self):
        return self.title

