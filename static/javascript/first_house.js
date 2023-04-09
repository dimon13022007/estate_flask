$(document).ready(function() {
  // Получаем список всех ссылок на изображения
  var $imgs = $('a[href^="#img"]');
  // Устанавливаем счетчик изображений
  var index = 0;

  // Обрабатываем клик по ссылке на изображение
  $imgs.on('click', function() {
    // Получаем ID изображения из атрибута href
    var id = $(this).attr('href');
    // Получаем элемент с ID, который соответствует нажатой ссылке
    var $popup = $(id);
    // Получаем ширину и высоту окна просмотра
    var wWidth = $(window).width();
    var wHeight = $(window).height();

    // Устанавливаем положение изображения по центру экрана
    $popup.find('.full-img').css({
      'top': (wHeight / 2) - ($popup.find('.full-img').height() / 2),
      'left': (wWidth / 2) - ($popup.find('.full-img').width() / 2)
    });

    // Показываем окно с изображением
    $popup.show();

    // Обрабатываем нажатие на кнопку закрытия
    $popup.find('.close').on('click', function() {
      // Скрываем окно с изображением
      $popup.hide();
      // Очищаем значение счетчика изображений
      index = 0;
    });

    // Обрабатываем нажатие на клавиши клавиатуры
    $(document).on('keydown', function(e) {
      if (e.keyCode === 37) { // Если нажата клавиша влево
        e.preventDefault();
        index--;
        // Если счетчик меньше нуля, переключаемся на последнее изображение
        if (index < 0) {
          index = $imgs.length - 1;
        }
        // Получаем ссылку на предыдущее