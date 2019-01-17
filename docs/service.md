# Vulcan Service

The VulcanService base class enforces a the basic methods required to create
a _serve-able_ resource. Your class, which should inherit from VulcanService
is expected to implement [init](#vulcanserviceinit), [fetch_one](#vulcanservicefetch_one), and [fetch_all](#vulcanservicefetch_all).

All VulcanService methods have a defined-optional argument called a
`context`. Within `context`, a requester of your service can provide additional information about the request
and how it should be fulfilled. For example, in a clinical application, it is likely important to know what
facility or patient specifically is in question. Context is where we provide those details. For more details on the `context` object, read on.

## VulcanService Instance Methods

---

## VulcanService.init

Your VulcanService is required to implement an `init` method, which returns enough data to satisfy
the initial rendering or utilization of your resource. For example, if you were modeling a news application like HackerNews, your init method should return enough data to render the front page of the HackerNews.

```python
from vulcan.service import VulcanService

class HackerNews(VulcanService):
    def init(self, context):
        articles = [
            {'title': 'BlockChain down 45%', ...},
            {'title': 'I let a ML model decide what I ate for a week...', ...},
            ...
        ]
        return articles
```

## VulcanService.fetch_one

TODO

## VulcanService.fetch_all

TODO
