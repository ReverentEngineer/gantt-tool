# gantt-tool

A Gantt chart generator that uses a YAML-based description document

## Description Language

### activities

`activities` is a list of activities to be done within the Gantt timeline. All
`activities` have a `name` which is used to describe the activity in the chart,
a `from` which is the start time of the activity, and a `to` which is the end
time of the activity.
