package com.example.basic.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.example.basic.database.entity.DrunkEntity;
import com.example.basic.database.entity.IceEntity;
import com.example.basic.database.entity.TmzoneEntity;
import com.example.basic.database.entity.WebEntity;
import com.example.basic.service.DrunkService;
import com.example.basic.service.IceService;
import com.example.basic.service.TmzoneService;
import com.example.basic.service.WebService;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@Controller
public class WebController {

    @Autowired
    private WebService webService;
    @Autowired
    private IceService iceService;
    @Autowired
    private DrunkService drunkService;
    @Autowired
    private TmzoneService tmzoneService;

    @GetMapping("/index")
    public String index(Authentication authentication, Model model) {
        List<IceEntity> iceList = iceService.selectAll();
        List<DrunkEntity> drunkList = drunkService.selectAll();
        List<TmzoneEntity> tmzoneList = tmzoneService.selectAll();

        log.info("[IceController][selectAll] Start");
        log.info("iceList: " + iceList.size());

        model.addAttribute("iceList", iceList);
        model.addAttribute("drunkList", drunkList);
        model.addAttribute("tmzoneList", tmzoneList);
        if (authentication != null) {
        UserDetails userDetails = (UserDetails) authentication.getPrincipal();
        model.addAttribute("username", userDetails.getUsername());
        }

        log.info("[WebController][index] Start");
        return "index";
    }

    @GetMapping("/index2")
    public String index2(Model model) {
        List<IceEntity> iceList = iceService.selectAll();
        List<DrunkEntity> drunkList = drunkService.selectAll();
        List<TmzoneEntity> tmzoneList = tmzoneService.selectAll();

        log.info("[IceController][selectAll] Start");
        log.info("iceList: " + iceList.size());

        model.addAttribute("iceList", iceList);
        model.addAttribute("drunkList", drunkList);
        model.addAttribute("tmzoneList", tmzoneList);

        log.info("[WebController][index2] Start");
        return "index2";
    }
    @GetMapping("/logout")
    public String logout(HttpServletRequest request) {
        log.info("[WebController][logout] Start");

        HttpSession session = request.getSession();
        session.removeAttribute("userId");
        session.removeAttribute("userRole");

        return "index2";
    }

    @GetMapping("/loginPage")
    public String loginPage() {
        log.info("[WebController][loginPage] Start");
        return "login";
    }

    @GetMapping("/join")
    public String join() {
        log.info("[WebController][join] Start");
        return "join";
    }

    @PostMapping("/join")
    public String join(@ModelAttribute WebEntity entity) {

        webService.joinUserDto(entity);
        return "redirect:/loginPage";
    }

    @GetMapping("/user")
    public String user() {
        log.info("[WebController][user] Start");
        return "user";
    }

    @GetMapping("/admin")
    public String admin() {
        log.info("[WebController][admin] Start");
        return "admin";
    }

    @GetMapping("/home")
    public String css() {
        return "css";
    }

    @GetMapping("/loginfail")
    public String loginfail() {
        return "loginfail";
    }
}
