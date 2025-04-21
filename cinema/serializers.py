from rest_framework import serializers
from cinema.models import Order, Ticket, MovieSession

class TicketSerializer(serializers.ModelSerializer):
    movie_session = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = ('id', 'row', 'seat', 'movie_session')

    def get_movie_session(self, obj):
        return {
            "id": obj.movie_session.id,
            "show_time": obj.movie_session.show_time,
            "movie_title": obj.movie_session.movie.title,
            "cinema_hall_name": obj.movie_session.cinema_hall.name,
            "cinema_hall_capacity": obj.movie_session.cinema_hall.capacity
        }

class OrderSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'tickets', 'created_at')
