create table if not exists users
(
    `id` Int64,
    `name` String,
    `email` String,
    `phone` FixedString(25),
    `created` DateTime,
    `modified` DateTime
)
engine = ReplacingMergeTree(modified)
order by id;