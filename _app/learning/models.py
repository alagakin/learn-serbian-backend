from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

from learn_serbian.utils import learned_percent
from topics.models import Topic
from words.models import Word


class SavedWord(models.Model):
    user = models.ForeignKey(
        get_user_model(), related_name="saved", on_delete=models.CASCADE
    )
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    last_repetition = models.DateTimeField(null=True, blank=True)
    repetition_count = models.PositiveSmallIntegerField(default=0)
    watched_at = models.DateTimeField(null=True, blank=True)
    watched_count = models.PositiveSmallIntegerField(default=0)
    skipped = models.BooleanField(default=False)

    @property
    def learned_percent(self):
        return learned_percent(self)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save(update_fields=["deleted"])

    def __str__(self):
        return str(self.word) + " - " + str(self.user)

    class Meta:
        unique_together = ["user", "word"]

    def save(self, *args, **kwargs):
        max_value = 5
        if self.repetition_count > max_value:
            self.repetition_count = max_value
        super().save(*args, **kwargs)


class Lesson(models.Model):
    user = models.ForeignKey(
        get_user_model(), related_name="lessons", on_delete=models.CASCADE
    )
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    saved_words = models.ManyToManyField(SavedWord, related_name="lessons",
                                         null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.topic) + " - " + str(self.user)

    @property
    def is_complete(self):
        return self.finished_at is not None
