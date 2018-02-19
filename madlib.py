
story = '''{0} was {1} down the road. {0} biggest fear was {1}.
{0} is a very compitent person when it came to {1}
, but it all depended on if {0} had the {3} to complete a task.
 {0} had a {2} and this made {0} very {3}.
 {0} needed to decide weather the {2} was going to be a {3} idea.
 Also {1} made {0} wonder about more important things like the {2}.
The clothes {0} wore were also {3} and made people think {3} of {0}.
{0} frankly didn't care because at the end {0} had a {2}. '''
name = raw_input("enter a name")
verb = raw_input("enter a verb")
noun = raw_input("enter a noun")
adjective = raw_input("enter an adjective")
name = raw_input("enter a name 
adjusted = story.format(name, verb, noun, adjective)

print(adjusted)
