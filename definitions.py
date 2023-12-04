# Contains the attributes used by Beautiful Soup to parse the page components

#MAIN_PAGE_LAST = {'title': 'Go to last page'}
MAIN_PAGE_LAST = {'aria-label': 'Last page'}
#MAIN_PAGE_RELEASE = {'class': 'views-field views-field-title'}
MAIN_PAGE_RELEASE = {'class': 'news-content-listing node-press-release'}
#PAGE_TEXT = {'class': 'field field--name-field-pr-body field--type-text-long field--label-hidden'}
PAGE_TEXT = {'class': 'field-formatter--text-default field-text-format--wysiwyg text-formatted field_body'}
#PAGE_TEXT = {'class': 'text-align-justify'}
#PAGE_TITLE = {'href': 'node-titlse'}
PAGE_TITLE = {'class': 'field-formatter--string'}
PAGE_DATE = {'class': 'node-updated-date'}
PAGE_TOPIC_LIST = {'class': 'field field--name-field-pr-topic field--type-taxonomy-term-reference field--label-above'}
PAGE_TOPIC = {'class': 'field__item'}
PAGE_COMPONENT_LIST = {'class': 'field field--name-field-pr-component field--type-taxonomy-term-reference field--label-above'}
PAGE_ID_CONTAINER = {'class': 'field field--name-field-pr-number field--type-text field--label-above'}
PAGE_ID = {'field__item'}