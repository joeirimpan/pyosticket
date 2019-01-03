# -*- coding: utf-8 -*-

"""Main module."""
import atexit

import requests

__all__ = ['OSTicketAPI', 'TicketModel']


class OSTicketAPI(object):

    def __init__(self, url, api_key):
        self.url = url

        self.session = requests.Session()
        atexit.register(self.session.close)

        self.session.headers["X-API-Key"] = api_key

    @property
    def ticket(self):
        return Ticket(connection=self)


class TicketModel(object):

    __slots__ = [
        "source", "name", "email", "ip",
        "subject", "topic_id", "attachments"
    ]

    def __init__(self, name, email, subject, topic_id, attachments, **kwargs):
        self.source = kwargs.get("source", "API")
        self.name = name
        self.email = email
        self.ip = kwargs.get("ip", "")
        self.subject = subject
        self.topic_id = topic_id
        self.attachments = attachments

    def to_dict(self):
        return {
            "source": self.source,
            "name": self.name,
            "email": self.email,
            "ip": self.ip,
            "subject": self.subject,
            "topicId": self.topic_id,
            "message": self.message,
            "attachments": self.attachments
        }


class Ticket(object):

    def __init__(self, connection):
        self.connection = connection

    @property
    def url(self):
        return self.connection.url

    def _raise_or_return_json(self, response):
        """Raise HTTPError before converting response to json

        :param response: Request response object
        """
        response.raise_for_status()

        try:
            json_value = response.json()
        except ValueError:
            return response.content, response.status_code
        else:
            return json_value, response.status_code

    def create(self, ticket):
        """Create a ticket

        :param ticket: An instance of `TicketModel`
        """
        response = self.connection.session.post(
            "%s/api/tickets.json" % self.url,
            json=ticket.to_dict(),
        )
        return self._raise_or_return_json(response)

    def all(self, email):
        """XXX: Custom API to fetch all tickets for this email

        :param email: Email of the user
        """
        response = self.connection.session.get(
            "%s/api/tickets/all" % self.url,
            params={"email": email},
        )
        return self._raise_or_return_json(response)

    def get(self, ticket_number, email):
        """XXX: Custom API to fetch a specific ticket

        :param ticket_number: Ticket number
        :param email: Email of the user
        """
        response = self.connection.session.get(
            "%s/api/tickets/%s" % (self.url, ticket_number),
            params={"email": email},
        )
        return self._raise_or_return_json(response)
