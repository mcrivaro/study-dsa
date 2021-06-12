class HashTable {
    constructor(size) {
        this.data = new Array(size);
    }

    _hash(key) {
        let hash = 0;
        for (let i = 0; i < key.length; i++) {
            hash = (hash + key.charCodeAt(i) * i) % this.data.length
        }
        return hash;
    }
    set(key, value) {
        const address = this._hash(key)
        const bucket = [key, value]
        // a bucket is the key/value pair that lies in the memory location indicated by the hash. it can contain multiple [key/value] pairs in case of hash collisions
        if (!this.data[address]) {
            this.data[address] = []
        }
        this.data[address].push(bucket)

    }
    get(key) {
        const address = this._hash(key)
        let bucket = this.data[address]
        let value = undefined
        for (const bucketItem of bucket) {
            if (bucketItem[0] == key) {
                value = bucketItem[1]
            }
        }
        console.log(value)
        return value
    }
}

const myHashTable = new HashTable(50);
myHashTable.set('grapes', 10000)
myHashTable.get('grapes')
myHashTable.set('apples', 9)
myHashTable.get('apples')
