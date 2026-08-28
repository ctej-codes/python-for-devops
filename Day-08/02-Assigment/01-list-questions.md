# Basic-Level List Questions

**Q1: What is a list in Python, and how is it used in DevOps?**
Ans: A list is collection type data type and it is heterogeneus it means that list can be stored with any data type. For example, string, int, float etc., In devops perspective it is used to store the list of s3 bucket names etc.,

**Q2: How do you create a list in Python, and can you provide an example related to DevOps?**
Ans: We can create a list in python by using a []
example: s3_buckets = ["charan", "tej"]

**Q3: What is the difference between a list and a tuple in Python, and when would you choose one over the other in a DevOps context?**
Ans: A list is mutable and a tuple is immutable.
Mutable: List can be modified and like new elements can be added or removed by using "append()" and "remove()"
Immutable: The new elements cannot be added and existing elements cannot be removed.

A list can be used when we want to add list os ec2 machine names, s3 bucket names etc.,
A tuple can be used to store the name of the admins of an AWS account in a case where the admins details should not be altered.

**Q4: How can you access elements in a list, and provide a DevOps-related example?**

Ans: A list can be accessed by using it's index value
Example: s3_buckets = ["charan_bucket", "tej_bucket", "vadepalli_bucket"]
To access the tej_bucket from s3_buckets list use s3_buckets[1]

**Q5: How do you add an element to the end of a list in Python? Provide a DevOps example.**
Ans: By using append()

```python
s3_buckets = ["charan_bucket", "tej_bucket", "vadepalli_bucket"]
servers.append('app-bucket')
```

**Q6: How can you remove an element from a list in Python, and can you provide a DevOps use case?**
Ans: By using remove()
```python
s3_buckets = ["charan_bucket", "tej_bucket", "vadepalli_bucket"]
servers.append('tej_bucket')
```

