const cluster = function(points, x0, y0, zoom) {

    const size = 200 / zoom;
    const xMin = x0 - size / 2;
    const xMax = x0 + size / 2;
    const yMin = y0 - size / 2;
    const yMax = y0 + size / 2;

    const cells = [];
    for (let i = 0; i < 10; i++) {
        for (let j = 0; j < 10; j++) {
            cells.push({
                i,
                j,
                count: 0,
                xMin: xMin + i * size / 10,
                xMax: xMin + (i + 1) * size / 10,
                yMin: yMin + j * size / 10,
                yMax: yMin + (j + 1) * size / 10,
            });
        }
    }

    for (const point of points) {
        for (const cell of cells) {
            if (point.x >= cell.xMin && point.x < cell.xMax && point.y >= cell.yMin && point.y < cell.yMax) {
                cell.count++;
                break;
            }
        }
    }

    const result = cells.filter(cell => cell.count > 0)
                        .map(({ i, j, count }) => ({ i, j, count }));

    result.sort((a, b) => {
        if (a.j !== b.j) {
            return a.j - b.j;
        } else {
            return a.i - b.i;
        }
    });

    return result;
};

const points = [
    { x: -50, y: -50 },
    { x: -50, y: -50 },
    { x: 0, y: 0 },
    { x: 50, y: 50 },
    { x: 50, y: 50 },
];

const result = cluster(points, 0, 0, 2);
console.log(result);