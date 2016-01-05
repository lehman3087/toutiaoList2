/**
 * Created by guizhouyuntushidai on 16/1/5.
 */
 $(function (){
       // { $("#example_left").popover({title: '文章链接', content: '123'});

            $('.example_left').on('click', function () {
                                $.alert({
                                    title: '链接地址',
                                    content: $(this).attr('data'),
                                    confirmButton: '确认',
                                    confirmButtonClass: 'btn-primary',
                                    icon: 'fa fa-info',
                                    animation: 'zoom',
                                    confirm: function () {
                                       // alert('Okay action clicked.');
                                    }
                                });
                            });

 });