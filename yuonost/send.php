<?php 

if (isset($_POST['submit']) && $_POST['name']=='') {
	$to = "info@un-moscow.ru";
	$to_copy = "innaysemenova@yandex.ru";
	//$from = "-f yfeoktistov1977@mail.ru"; // Здесь нужно написать e-mail, от кого будут приходить письма
	$first_name = $_POST['first_name'];
	$subject = "Сообщение с сайта un-moscow.ru для тренера";
	//$subject2 = "Copy of your form submission";
	$message = "ФИО посетителя: ". $first_name . "\n Контактный телефон "  . $_POST['phone'] . "\n Сообщение для тренера: " . $_POST['message'];

	mail($to_copy, $subject, $message);
	$res = mail($to, $subject, $message);
	if($res = true) {
		echo "Сообщение отправлено. Спасибо Вам " . $first_name . ", мы скоро свяжемся с Вами.";
		echo "<br /><br /><a href='http://un-moscow.ru/'>Вернуться на сайт.</a>";
	}
}

?>
<!--Переадресация на главную страницу сайта, через 3 секунды-->
<script language="JavaScript" type="text/javascript">
	function changeurl() {
		eval(self.location="http://un-moscow.ru/");
	}
	window.setTimeout("changeurl();", 5000);
</script>