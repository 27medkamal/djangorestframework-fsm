djangorestframework-fsm
===================

Automatically hook your Django-FSM transitions up to Django REST Framework

Based on [drf-fsm-transitions](https://github.com/jacobh/drf-fsm-transitions) which is very outdated and does not support a lot of the functionality described below

## Installation

```bash
pip install djangorestframework-fsm
```


## Usage

When declaring your viewset, simply mix in the result of `get_drf_fsm_mixin`

```python
from rest_framework import viewsets
from djangorestframework_fsm.viewset_mixins import get_drf_fsm_mixin

from .models import Article


class ArticleViewSet(
    get_drf_fsm_mixin(Article, fieldname='state'),
    viewsets.ModelViewSet,
):
    queryset = Article.objects.all()
```

You can customise the field name as show above. By default, it uses `state`

if `Article` had 2 transitions, `delete` and `publish`, the following API calls would be set up

- `POST /api/article/1234/delete/`
- `POST /api/article/1234/publish/`


In addition, a possible transitions endpoint is provided

- `GET /api/article/1234/possible-transitions/` -> returns the transitions that satisfy fsm's `can_proceed`

### Custom transition arguments

Passing custom arguments to each transition can be done by specifying them in the `get_{}_kwargs` method:

```python
class ArticleViewSet(
    get_drf_fsm_mixin(Article, fieldname='state'),
    viewsets.ModelViewSet,
):
    queryset = Article.objects.all()
    
    def get_publish_kwargs(self):
        return {
            'publisher_address': self.request.data.get('publisher_address', ''),
        }
```

This will in turn call the `Article.publish` method with the `publisher_address` argument

In addition, `djangorestframework-fsm` automatically calls the transition method with a `by` argument if the method accepts one unless it's overriden in the `get_{}_kwargs` viewset method
### Saving

By default, the model instance will be saved after the transition has been successfully called. This can be disabled with the `save_after_transition` attribute

```python
class ArticleViewSet(
    get_drf_fsm_mixin(Article),
    viewsets.ModelViewSet,
):
    queryset = Article.objects.all()
    save_after_transition = False
```

### Permissions

Custom permissions should be defined on the model's transition method


