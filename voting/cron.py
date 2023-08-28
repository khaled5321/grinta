import kronos
from .services import push_notification_send
from .models import Competition


@kronos.register("* * * * *") # cron job that runs every minute
def check_if_competiton_end():
    competitions = Competition.objects.filter(is_finished=False)
    for competition in competitions:
        if competition.has_ended:
            competition.is_finished = True
            competition.save()
            push_notification_send(competition_name=competition.name, winner=competition.winner)