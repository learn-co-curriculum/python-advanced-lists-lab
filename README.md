
# Python Lists - Reloaded

## Introduction:

A `List` is a fundamental data type in Python. It is used to group elements together in order. Each element is separated by a comma and can be any data type. In this lab, we will practice using lists and builtin methods Python provides for using and manipulating lists.

## Objectives:

* Gain comfort and familiarity with iterating over lists
* Recreate some commonly used methods that iterate through lists and return a desired result

## Iterating On Each Element

A common use for lists is to group together each element of a set or subset. Usually there will be times where we will want to have direct access to a group of elements and be able to query or change each of the elements. For instance, we have a list of people (our group of 'elements') who are all going to the same housewarming party. Each person has an RSVP status attribute. To check each person's status, we will need to iterate through each element and access their status.

```python
housewarming_invitees = [{'name': "Jen", 'rsvp': "Yes"}, {'name': "Mike", 'rsvp': "No"}, {'name': "Henry", 'rsvp': "Yes"}, {'name': "Anna", 'rsvp': "No"}]
for invitee in housewarming_invitees:
    print(invitee['rsvp'])
```

Great, we can query each element, but let's say we need to send a list of the guest's names to a company that is going to make seating cards with each guests' name? We don't want to re-write all the names, but we don't want to just iterate through and blindly send over a list of names without making sure that they are all capitalized properly. So, We need to iterate through each element and titlize each person's name.

```python
housewarming_invitees = [{'name': "Jen", 'rsvp': "Yes"}, {'name': "Mike", 'rsvp': "No"}, {'name': "Henry", 'rsvp': "Yes"}, {'name': "Anna", 'rsvp': "No"}]

def titlize_names(list_of_invitees): 
    return [invitee['name'].title() for invitee in list_of_invitees]
```

Now what if we would like to find an element that meets a certain criteria? For example, if we only wanted to find the guest with the name "Jen". 

What about wanting to find only the guests who have RSVPd "Yes" to the Party? 

Open `list_methods.py` and complete the functions provided according to their descriptions which are noted in comments.

## List Comprehension

> **Note:** When working through the lab, remember to make use of list comprehension as is it can often be a more concise and simple method to solve these types of problems. To break down exactly how list comprehension works, see the example below:

```python

new_list = []
for element in elements:
    new_list.append(element['name'])
    
# In list comprehension we create a new list, then we declare what operation we want to perform on each element, then we define what the element will be called and finally we define the list on which we are iterating.

[element['name'] for element in elements]

# no need to append as we are already returning the value directly inside the list
```

# Summary

In this lab, we practiced iterating on lists. We looked at how to break down the logic for each step of the operation and what questions we would like to solve for using iterators and lists. We looked at lists that contained elements of different data types. We also wrote our own functions to immitate some already built-in list methods as well as some functions that perform commonly used operations.

For more information on built-in `list` functions in Python, [click here.](https://docs.python.org/2/library/functions.html#max)
