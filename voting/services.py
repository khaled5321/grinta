from rest_framework import exceptions
from django.shortcuts import get_object_or_404
from accounts.models import User
from .models import Competition, Vote, Singer


def competition_get(*, competition_id:int) -> Competition:
    competition = get_object_or_404(Competition, id=competition_id)
    return competition


def singer_get(*, singer_name:str) -> Singer:
    singer = get_object_or_404(Singer, name=singer_name)
    return singer

def vote(*, user: User, competition: Competition, singer: Singer) -> Vote:
    if competition.has_ended:
        raise exceptions.ValidationError("Competition has ended")
    
    if Vote.objects.filter(voter=user, competition=competition).exists():
        raise exceptions.ValidationError("You have already voted for this competition")

    vote = Vote.objects.create(voter=user, competition=competition, vote_for = singer)

    return vote

def push_notification_send(*, competition_name:str, winner: str)-> None:
    if winner == "draw":
        print(f"Competition {competition_name} Ended, it's a draw")
        return

    print(f"Competition {competition_name} Ended, singer {winner} is the winner")