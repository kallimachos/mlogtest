use test;
// db.getMongo().forceWriteMode('legacy');
// db.getMongo().forceWriteMode('commands');
print("Write mode: " + db.getMongo().writeMode());


/// MTEST-insert

// setup
var x = 1;
var coll = 'MTEST-insert';

// Vanilla insert
db[coll].insert({_id: x, name: "insert"});

// w:0
x += 1;
db[coll].insert({_id: x, name: "insert"}, {writeConcern: {w: 0}});

// w:1
x += 1;
db[coll].insert({_id: x, name: "insert"}, {writeConcern: {w: 1}});

// Shell converts array insert into a bulk write
coll = 'MTEST-bulkinsert';
x += 1;
var doc1 = {_id: x, name: "bulkinsert"};
x += 1;
var doc2 = {_id: x, name: "bulkinsert"};
x += 1;
var doc3 = {_id: x, name: "bulkinsert"};
x += 1;
var doc4 = {_id: x, name: "bulkinsert"};
db[coll].insert([doc1, doc2, doc3, doc4]);


/// MTEST-query

// setup
coll = 'MTEST-query';
x += 1;
var doc = {_id: x, name: "query"};
db[coll].insert(doc);
var result;

// COLLSCAN
result = db[coll].find({name: "query"});

// IXSCAN
result = db[coll].find(doc);

// Fast COUNT
result = db[coll].count();

// COUNT w/ criteria
result = db[coll].count({counter:1});

// Slow query
result = db[coll].find({ $where: 'sleep(101) || true'});


/// MTEST-update

// setup
coll = 'MTEST-update';
x += 1;
doc = {_id: x, name: "update"};
db[coll].insert(doc);

// UPDATE
db[coll].update(doc, {$set: {counter: 1}});

// UPDATE w/ upsert
db[coll].update(doc, {$inc: { counter: 1}}, { upsert: true});

//findAndModify
db[coll].findAndModify({
    query: doc,
    update: {
        $inc: { counter: 1 }
    }
});


/// MTEST-delete

// setup
coll = 'MTEST-delete';
x += 1;
doc = {_id: x, name: "delete"};
db[coll].insert(doc);

// REMOVE
db[coll].remove(doc);
