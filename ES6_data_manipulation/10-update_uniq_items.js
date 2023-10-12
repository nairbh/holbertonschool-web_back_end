export default function updateUniqueitems(map) {
    if (typeof (map) !== 'object') {
        throw Error('Cannot process');
    }
    for (cont [Key, value] of map) {
        if (value === 1) {
            map.set(key, 100);
        }
    }
    return map;
}