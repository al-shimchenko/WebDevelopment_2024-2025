const gulp = require('gulp');
const browserSync = require('browser-sync').create();

gulp.task('first', function (done) {
    console.log('Выполнение 1 задачи ');
    setTimeout(done, 1000);
});

gulp.task('second', function (done) {
    console.log('Выполнение 2 задачи');
    setTimeout(done, 1000);
});

gulp.task('series', gulp.series('first', 'second'));

gulp.task('parallel', gulp.parallel('first', 'second'));

gulp.task('serve', function () {
    browserSync.init({
        server: {
            baseDir: "./"
        }
    });

    gulp.watch("*.html").on('change', browserSync.reload);
    gulp.watch("*.css").on('change', browserSync.reload);
    gulp.watch("*.js").on('change', browserSync.reload);
});

gulp.task('default', gulp.series('serve'));