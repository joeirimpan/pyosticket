## PyOSTicket

![](https://img.shields.io/pypi/v/pyosticket.svg?style=for-the-badge)


Python client for os ticket


```python
from pyosticket import OSTicketAPI, TicketModel

osticket = OSTicketAPI(url="URL", api_key="API-KEY")

# XXX Custom endpoints
osticket.ticket.all("email@email.com")
osticket.ticket.get("XXXXXXXXXXX", "email@email.com")

# create ticket
ticket = TicketModel(**{
    "name": "John Doe",
    "email": "johndoe@lorem.com",
    "subject": "Lorem Ipsum",
    "topicId": "1",
    "message": "data:text/html,Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam lobortis sagittis turpis vel bibendum. Nunc eget tincidunt leo. Suspendisse a nibh vulputate, ultrices leo mollis, maximus nisl.",
    "attachments": [{
        "filename.png": "data:image/png;base64,BASE64_ENCODED_IMAGE_HERE"
    }]
})
osticket.ticket.create(ticket)
```
