// Simple SM-2 implementation
function calculateSM2(quality, repetitions, easiness, interval) {
    if (quality < 3) {
        repetitions = 0;
        interval = 1;
    } else {
        if (repetitions === 0) interval = 1;
        else if (repetitions === 1) interval = 6;
        else interval = Math.round(interval * easiness);
        repetitions++;
    }
    
    easiness = easiness + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02));
    if (easiness < 1.3) easiness = 1.3;
    
    return { repetitions, easiness, interval };
}
